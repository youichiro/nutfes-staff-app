from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from config.manual_urls import *


class ManualLinksView(LoginRequiredMixin, TemplateView):
    template_name = 'manual/manual_links.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['manual1'] = manual1_url
        context['manual2'] = manual2_url
        context['manual3'] = manual3_url
        return context
