from django.urls import path
from . import views


urlpatterns = [
    path('', views.MessageListView.as_view(), name='message_view'),
    path('form/', views.MessageCreateView.as_view(), name='message_form'),
    path('<int:id>/reply_form/', views.ReplyCreateView.as_view(), name='reply_form'),
]
