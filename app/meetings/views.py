from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime

from meetings.models import Meeting
from schedule import next_second_monday


def meetings_list(request):
    meeting_list = Meeting.objects.order_by("-date")
    page = request.GET.get("page", 1)
    paginator = Paginator(meeting_list, 40)
    try:
        meetings = paginator.page(page)
    except PageNotAnInteger:
        meetings = paginator.page(1)
    except EmptyPage:
        meetings = paginator.page(paginator.num_pages)
    context = {"meetings": meetings, "page_title": "Meeting list"}
    return render(request, "meeting_list.html", context)


def _meeting_tba(request):
    next_meeting_date = next_second_monday()
    return render(request, "tba.html", {"meeting_date": next_meeting_date})


def _render_meeting(meeting: Meeting, request):
    context = {"meeting": meeting}
    if meeting.announcement is not None:
        context["message"] = meeting.announcement
    return render(request, "meeting.html", context)


def next_meeting_page(request):
    try:
        meeting = Meeting.objects.order_by("-date").first()
    except Meeting.DoesNotExist:
        return _meeting_tba(request)
    if meeting.date.date() < datetime.now().date():
        return _meeting_tba(request)
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
