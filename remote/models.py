from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    message = models.TextField(max_length=100000000, blank=True, default='{}')
    message_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


class Command(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    command = models.CharField(max_length=100000000, blank=True, default='{}')
    command_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


class Script(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    Script = models.TextField(max_length=100000000, blank=True, default='{}')
    script_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


