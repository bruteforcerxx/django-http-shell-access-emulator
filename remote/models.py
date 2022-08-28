from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=400, blank=True)
    serial_num = models.CharField(max_length=400, blank=True,)
    uid = models.CharField(max_length=400, default='0000000AAAAAAAAA')
    ip = models.CharField(max_length=400, default='')
    last_seen = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=1048576, blank=True, default='[]')
    message_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    active = models.CharField(max_length=400, blank=True, default='True')
    short_cuts = models.TextField(max_length=1048576, blank=True, default='[]')
    objects = None

    def __str__(self):
        return str(self.user)


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    alert = models.TextField(max_length=1048576, blank=True, default='[]')
    alert_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str('Alerts')


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    message = models.TextField(max_length=1048576, blank=True, default='[]')
    message_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


class Command(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    command = models.CharField(max_length=10485760, blank=True, default='[]')
    command_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


class CommandResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    command = models.CharField(max_length=10485760, blank=True, default='[]')
    command_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


class Script(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    iden = models.CharField(max_length=400, blank=True, )
    Script = models.TextField(max_length=10485760, blank=True, default='[]')
    script_count = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    objects = None

    def __str__(self):
        return str(self.user)


