from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime

from meetings.models import Meeting
from schedule import get_next_meeting_time, make_when


def meetings_list(request):
    meeting_list = Meeting.objects.order_by("-date")
    page = request.GET.get("page", 1)
    paginator = Paginator(meeting_list, 30)
    try:
        meetings = paginator.page(page)
    except PageNotAnInteger:
        meetings = paginator.page(1)
    except EmptyPage:
        meetings = paginator.page(paginator.num_pages)
    context = {"meetings": meetings, "page_title": "Meeting list"}
    return render(request, "meeting_list.html", context)


def _render_tba(request):
    next_time = get_next_meeting_time()
    next_meeting_str = make_when(next_time)
    return render(request, "tba.html", {"when": next_meeting_str})


def _render_meeting(meeting: Meeting, request):
    context = {"meeting": meeting}
    if meeting.announcement is not None:
        context["message"] = meeting.announcement
    return render(request, "meeting.html", context)


def next_meeting_page(request):
    try:
        # sorted ascending (order_by("date"))
        upcoming_meetings = Meeting.objects.order_by("date").filter(
            date__gte=datetime.now().date()
        )
        meeting = upcoming_meetings[0]
    except IndexError:
        return _render_tba(request)
    return _render_meeting(meeting, request)


def meeting_page(request, pk: int = None):
    date_query = request.GET.get("date")
    if date_query:
        meetings = Meeting.objects.filter(date=date_query)
        if len(meetings) == 1:
            return render(request, "meeting.html", {"meeting": meetings[0]})
        else:
            return HttpResponse(status=400)
    meeting = Meeting.objects.get(pk=pk)
    return _render_meeting(meeting, request)
