from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShiftListView.as_view(), name='whole_shift'),
    path('<int:id>/', views.ShiftDetailView.as_view(), name='personal_shift'),
    path('my_shift/', views.MyShiftView.as_view(), name='my_shift'),
]
