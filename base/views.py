from django.shortcuts import render
from django.http import HttpResponse
from .models import Host, Status


def home(request):
    hosts = Host.objects.filter(owner__username='admin')
    # statuses = Status.objects.filter(server_id=hosts)
    statuses = Status.objects.filter(server_id=-1)  # TODO: update the line

    for host in hosts:
        # statuses = statuses | Status.objects.filter(server_id=host.id)
        statuses = statuses | Status.objects.filter(server_id=host.id)

    context = {'hosts': hosts, 'statuses': statuses}

    return render(request, 'base/home.html', context)
