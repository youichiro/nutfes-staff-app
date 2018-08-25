from django.urls import path
from . import views


urlpatterns = [
    path('1/', views.manual1_view, name='manual1'),
    path('2/', views.manual2_view, name='manual2'),
    path('3/', views.manual3_view, name='manual3'),
]
