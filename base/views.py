from django.shortcuts import render
from django.http import HttpResponse
from .models import Host, Method


def home(request):
    return HttpResponse("Working!")
