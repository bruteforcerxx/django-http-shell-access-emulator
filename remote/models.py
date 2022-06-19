from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    objects = None

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']

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


