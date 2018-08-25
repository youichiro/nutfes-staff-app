from django.urls import path
from . import views


urlpatterns = [
    path('whole/', views.ShiftListView.as_view(), name='whole_shift'),
    path('<int:id>/', views.ShiftDetailView.as_view(), name='personal_shift'),
]
