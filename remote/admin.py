from django.contrib import admin
from .models import Messages, Command, Script, CommandResponse, UserData, Alert

# Register your models here.

admin.site.register(Messages)
admin.site.register(Command)
admin.site.register(Script)
admin.site.register(CommandResponse)
admin.site.register(UserData)
admin.site.register(Alert)