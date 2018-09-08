from django.urls import path
from . import views


urlpatterns = [
    path('', views.TimetableListView.as_view(), name='timetable'),
]
