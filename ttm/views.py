from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.
def index(request):
    event_list = Event.objects.order_by("-event_start")[:5]
    return render(request, "index.html", {"events": event_list})