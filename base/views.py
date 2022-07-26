from django.shortcuts import render
from django.http import HttpResponse
from .models import Hosts, Methods


def home(request):
    return HttpResponse("Working!")
