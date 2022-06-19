from django.contrib import admin
from .models import Messages, Command, Script

# Register your models here.

admin.site.register(Messages)
admin.site.register(Command)
admin.site.register(Script)
