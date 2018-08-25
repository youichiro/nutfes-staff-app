from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('account/', include('account.urls')),
    path('message/', include('message.urls')),
    path('shift/', include('shift.urls')),
]
