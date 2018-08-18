from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationForm


class UserCreateView(CreateView):
    template_name = 'account/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
