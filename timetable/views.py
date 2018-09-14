import datetime
from django.views.generic import ListView
from .models import Timetable
from .scripts.const import attr_to_str


def get_default_shift_id():
    now = datetime.datetime.now()
    date = now.date()
    if date == datetime.date(2018, 9, 15):
        return 2
    elif date == datetime.date(2018, 9, 16):
        return 4
    else:
        return 1


def get_time_now():
    now = datetime.datetime.now()
    if now.minute < 30:
        time_now = str(now.hour).rjust(2, '0') + ':00'
    else:
        time_now = str(now.hour).rjust(2, '0') + ':30'
    return time_now


def get_times_and_events(query):
    attr_list = [[attr_to_str[k], v] for k, v in query.__dict__.items() if k[0] == 't']
    times = [attr[0] for attr in attr_list]
    events = [attr[1] for attr in attr_list]
    time_flags = [1 if time == get_time_now() else 0 for time in times]
    return times, events, time_flags


def prepare_event_list(events, flags):
    events = [[event, flag] for event, flag in zip(events, flags)]
    events = events[::-1]
    count = 1
    flag_count = 0
    event_count = []
    for i, (event, flag) in enumerate(events):
        if i == 0:
            continue
        count = count + 1 if event == events[i - 1][0] else 1
        flag_count = flag_count + 1 if flag == 1 or (count > 1 and flag_count > 0) else 0
        event_count.append([event, count, flag_count])
    event_count = event_count[::-1] + [[events[0][0], 1, events[0][1]]]
    return event_count


class TimetableListView(ListView):
    model = Timetable
    template_name = 'timetable/timetable_list.html'

    def get_queryset(self):
        queryset = Timetable.objects.filter(sheet_id=get_default_shift_id())
        sheet_id_request = self.request.GET.get('sheet_id')
        if sheet_id_request:
            queryset = Timetable.objects.filter(sheet_id=sheet_id_request)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        queryset = self.get_queryset()

        first_query = queryset.first()
        times, _, flags = get_times_and_events(first_query)

        events_set = []
        for timetable in queryset:
            _, events, _ = get_times_and_events(timetable)
            events_set.append([timetable, prepare_event_list(events, flags)])
        events_set.sort(key=lambda x: x[0].place)

        context['times'] = zip(times, flags)
        context['events_set'] = events_set
        return context
