from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Shark

def home(request):
    return render(request, "home.html")

def about(request):
    return HttpResponse("<h1>About</h1>")

def list(request):
    sharks = Shark.objects.all()
    return render(request, "shark-list.html", { "sharks": sharks })

def show(request, id):
    shark = get_object_or_404(Shark, pk=id)
    return HttpResponse(f"<h1>{shark.name}</h1>")
    