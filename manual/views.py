from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from config.manual_urls import manual_dic


class ManualLinksView(LoginRequiredMixin, TemplateView):
    template_name = 'manual/manual_links.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['manual_dic'] = manual_dic
        return context
