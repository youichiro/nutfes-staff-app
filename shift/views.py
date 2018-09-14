import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import Shift
from .scripts.const import time_to_time


def get_default_shift_id():
    now = datetime.datetime.now()
    date = now.date()
    if date == datetime.date(2018, 9, 14):
        return 1
    elif date == datetime.date(2018, 9, 15):
        return 4
    elif date == datetime.date(2018, 9, 16):
        return 6
    elif date == datetime.date(2018, 9, 17):
        return 7
    else:
        return 3


def get_time_now():
    now = datetime.datetime.now()
    if now.minute < 30:
        time_now = str(now.hour).rjust(2, '0') + ':00'
    else:
        time_now = str(now.hour).rjust(2, '0') + ':30'
    return time_now


def get_times_and_tasks(query):
    attr_list = [[time_to_time[k], v] for k, v in query.__dict__.items() if k[0] == 't']
    times = [attr[0] for attr in attr_list]
    tasks = [attr[1] for attr in attr_list]
    time_flags = [1 if time == get_time_now() else 0 for time in times]
    return times, tasks, time_flags


def prepare_task_list(tasks, flags):
    tasks = [[task, flag] for task, flag in zip(tasks, flags)]
    tasks = tasks[::-1]
    count = 1
    flag_count = 0
    task_count = []
    for i, (task, flag) in enumerate(tasks):
        if i == 0:
            continue
        count = count + 1 if task == tasks[i - 1][0] else 1
        flag_count = flag_count + 1 if flag == 1 or (count > 1 and flag_count > 0) else 0
        task_count.append([task, count, flag_count])
    task_count = task_count[::-1] + [[tasks[0][0], 1, tasks[0][1]]]
    return task_count


def get_personal_shifts(user):
    shift1 = Shift.objects.filter(user=user, shift_id=1).first()
    shift2 = Shift.objects.filter(user=user, shift_id=2).first()
    shift3 = Shift.objects.filter(user=user, shift_id=3).first()
    shift4 = Shift.objects.filter(user=user, shift_id=4).first()
    shift5 = Shift.objects.filter(user=user, shift_id=5).first()
    shift6 = Shift.objects.filter(user=user, shift_id=6).first()
    shift7 = Shift.objects.filter(user=user, shift_id=7).first()
    return [shift1, shift2, shift3, shift4, shift5, shift6, shift7]


class ShiftListView(LoginRequiredMixin, ListView):
    model = Shift
    template_name = 'shift/shift_list.html'

    def get_queryset(self):
        queryset = Shift.objects.filter(shift_id=get_default_shift_id())
        shift_id_request = self.request.GET.get('shift_id')
        if shift_id_request:
            if int(shift_id_request) in list(Shift.objects.values_list('shift_id', flat=True)):
                queryset = Shift.objects.filter(shift_id=shift_id_request)
            else:
                queryset = None
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        queryset = self.get_queryset()
        if not queryset:
            return context

        first_query = queryset.first()
        times, _, flags = get_times_and_tasks(first_query)

        tasks_set = []
        for shift in queryset:
            _, tasks, _ = get_times_and_tasks(shift)
            tasks_set.append([shift, prepare_task_list(tasks, flags)])
        tasks_set.sort(key=lambda x: x[0].get_department().id)

        context['times'] = zip(times, flags)
        context['tasks_set'] = tasks_set
        return context


class ShiftDetailView(LoginRequiredMixin, DetailView):
    model = Shift
    template_name = 'shift/shift_detail.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        shift = self.get_object()
        times, tasks, flags = get_times_and_tasks(shift)
        context['times'] = zip(times, flags)
        context['tasks'] = prepare_task_list(tasks, flags)
        context['personal_shifts'] = get_personal_shifts(shift.user)
        return context


class MyShiftView(LoginRequiredMixin, TemplateView):
    template_name = 'shift/shift_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        if not Shift.objects.filter(user=user).exists():
            return
        shift = Shift.objects.filter(user=user, shift_id=get_default_shift_id()).first()
        times, tasks, flags = get_times_and_tasks(shift)
        context['shift'] = shift
        context['times'] = zip(times, flags)
        context['tasks'] = prepare_task_list(tasks, flags)
        context['personal_shifts'] = get_personal_shifts(user)
        return context
