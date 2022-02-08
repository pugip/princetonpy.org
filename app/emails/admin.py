from django.contrib import admin

from emails.models import EmailFailure


class EmailsAdmin(admin.ModelAdmin):
    list_display = ("raw_message", "failure_type")


admin.site.register(EmailFailure, EmailsAdmin)
