from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('message/', include('message.urls')),
    path('shift/', include('shift.urls')),
    path('manual/', include('manual.urls')),
    path('timetable/', include('timetable.urls')),
    path('', lambda r: HttpResponseRedirect('shift/my_shift/')),
]
