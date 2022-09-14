from django.shortcuts import render
from .models import Cv
# Create your views here.

def index(request):
    cv = Cv.objects.all().order_by("-startDate")
    context = {
        "cv": cv
        }
    return render(request, 'cv/index.html', context)