from django.views.generic import TemplateView
from homepage.models import MeetingLink
from homepage.schedule import next_second_monday


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            link_entry = MeetingLink.objects.latest("id")
            context["link_entry"] = link_entry
        except MeetingLink.DoesNotExist:
            pass
        context["next_meeting_date"] = next_second_monday()
        return context
