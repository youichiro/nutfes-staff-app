from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('message/', include('message.urls')),
    path('shift/', include('shift.urls')),
    path('manual/', include('manual.urls')),
]
