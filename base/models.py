from django.db import models
from django.contrib.auth.models import User


class Method(models.Model):
    method = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.method


class Host(models.Model):
    name = models.CharField(max_length=50)  # TODO: Update pony ORM
    description = models.CharField(max_length=150)
    server = models.CharField(max_length=100)
    port = models.IntegerField()
    method = models.ForeignKey(Method, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # TODO: Update pony ORM
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Status(models.Model):
    status = models.CharField(max_length=50)
    response_code = models.IntegerField()
    url = models.CharField(max_length=150)
    method = models.CharField(max_length=50)
    content_type = models.CharField(max_length=50)
    content_length = models.IntegerField()
    server_id = models.ForeignKey(Host, on_delete=models.SET_NULL, null=True)
    timestamp = models.TimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
