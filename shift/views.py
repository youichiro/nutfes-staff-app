from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import Shift
from .scripts.const import time_to_time


def prepare_task_list(tasks):
    tasks = tasks[::-1]
    count = 1
    task_count = []
    for i, task in enumerate(tasks):
        if i == 0:
            continue
        count = count + 1 if task == tasks[i - 1] else 1
        task_count.append([task, count])
    task_count = task_count[::-1] + [[tasks[0], 1]]
    return task_count


class ShiftListView(LoginRequiredMixin, ListView):
    model = Shift
    template_name = 'shift/shift_list.html'

    def get_queryset(self):
        default_shift_id = 1  # シフトの指定がない場合の表示するシフト
        queryset = Shift.objects.filter(shift_id=default_shift_id)
        shift_id_request = self.request.GET.get('shift_id')
        if shift_id_request:
            queryset = Shift.objects.filter(shift_id=shift_id_request)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        queryset = self.get_queryset()

        first_query = queryset.first()
        times = [time_to_time[k] for k in first_query.__dict__.keys() if k[0] == 't']
        context['times'] = times

        tasks_set = []
        for shift in queryset:
            tasks = [v for k, v in shift.__dict__.items() if k[0] == 't']
            tasks_set.append([shift, prepare_task_list(tasks)])
        tasks_set.sort(key=lambda x: x[0].get_department().id)
        context['tasks_set'] = tasks_set

        return context


class ShiftDetailView(LoginRequiredMixin, DetailView):
    model = Shift
    template_name = 'shift/shift_detail.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        shift = self.get_object()
        attr_list = [[time_to_time[k], v] for k, v in shift.__dict__.items() if k[0] == 't']
        times = [attr[0] for attr in attr_list]
        tasks = [attr[1] for attr in attr_list]

        shift1 = Shift.objects.filter(user=shift.user, shift_id=1).first()
        shift2 = Shift.objects.filter(user=shift.user, shift_id=2).first()
        shift3 = Shift.objects.filter(user=shift.user, shift_id=3).first()
        shift4 = Shift.objects.filter(user=shift.user, shift_id=4).first()

        context['times'] = times
        context['tasks'] = prepare_task_list(tasks)
        context['four_shift'] = [shift1, shift2, shift3, shift4]
        return context


class MyShiftView(LoginRequiredMixin, TemplateView):
    template_name = 'shift/shift_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        default_shift_id = 1  # シフトの指定がない場合の表示するシフト
        user = self.request.user
        if not user.is_authenticated:
            return
        if not Shift.objects.filter(user=user).exists():
            return
        shift = Shift.objects.filter(user=user, shift_id=default_shift_id).first()
        attr_list = [[time_to_time[k], v] for k, v in shift.__dict__.items() if k[0] == 't']
        times = [attr[0] for attr in attr_list]
        tasks = [attr[1] for attr in attr_list]

        shift1 = Shift.objects.filter(user=user, shift_id=1).first
        shift2 = Shift.objects.filter(user=user, shift_id=2).first
        shift3 = Shift.objects.filter(user=user, shift_id=3).first
        shift4 = Shift.objects.filter(user=user, shift_id=4).first

        context['shift'] = shift
        context['times'] = times
        context['tasks'] = prepare_task_list(tasks)
        context['four_shift'] = [shift1, shift2, shift3, shift4]

        return context
