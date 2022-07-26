from django.db import models
from django.contrib.auth.models import User


class Methods(models.Model):
    methods = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.methods


class Hosts(models.Model):
    name = models.TextField()
    server = models.TextField(null=True, blank=True)
    port = models.IntegerField()
    method = models.ForeignKey(Methods, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
