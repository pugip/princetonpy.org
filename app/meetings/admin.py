from django.contrib import admin

# Register your models here.
from meetings.models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ("date", "title")


admin.site.register(Meeting, MeetingAdmin)
