from django.shortcuts import redirect
from config.manual_urls import *


def manual1_view(request):
    return redirect(manual1_url)


def manual2_view(request):
    return redirect(manual2_url)


def manual3_view(request):
    return redirect(manual3_url)
