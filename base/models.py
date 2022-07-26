from django.db import models
from django.contrib.auth.models import User


class Method(models.Model):
    methods = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.methods


class Host(models.Model):
    name = models.CharField(max_length=50)
    server = models.CharField(max_length=50)
    port = models.IntegerField()
    method = models.ForeignKey(Method, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
