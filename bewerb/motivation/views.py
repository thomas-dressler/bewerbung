from django.shortcuts import render
from .models import Motivation
# Create your views here.

def index(request):
    current_user = request.user
    moti = Motivation.objects.get(assignedUser_id=request.user.id)
    context = {
        "moti": moti
        }
    return render(request, 'motivation/index.html', context)