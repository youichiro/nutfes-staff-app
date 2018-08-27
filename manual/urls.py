from django.urls import path
from . import views


urlpatterns = [
    path('', views.ManualLinksView.as_view(), name='manual')
]
