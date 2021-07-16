from django.contrib import admin

# Register your models here.
from homepage.models import MeetingLink


class MeetingLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'link_text')


admin.site.register(MeetingLink, MeetingLinkAdmin)
