from django.views.generic import ListView, DetailView
from .models import Shift


class ShiftListView(ListView):
    model = Shift
    template_name = 'shift/shift_list.html'


class ShiftDetailView(DetailView):
    model = Shift
    template_name = 'shift/shift_detail.html'
    pk_url_kwarg = 'id'
