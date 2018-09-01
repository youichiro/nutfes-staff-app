from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MessageForm, ReplyForm
from .models import Message, Reply


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message/message_list.html'
    queryset = model.objects.all().prefetch_related('reply_set')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'message/message_form.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_form')

    def form_valid(self, form):
        user = self.request.user
        message = form.save(commit=False)
        message.user = user
        message.save()
        return redirect('message_form')


class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    template_name = 'message/reply_form.html'
    form_class = ReplyForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('message_view')

    def form_valid(self, form):
        user = self.request.user
        message_id = self.kwargs.get('id')
        reply = form.save(commit=False)
        reply.user = user
        reply.message_id = message_id
        reply.save()
        return redirect('message_view')
