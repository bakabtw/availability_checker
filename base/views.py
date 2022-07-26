from django.shortcuts import render
from django.http import HttpResponse
from .models import Host, Method


def home(request):
    hosts = Host.objects.all()
    context = {'hosts': hosts}

    return render(request, 'base/home.html', context)
