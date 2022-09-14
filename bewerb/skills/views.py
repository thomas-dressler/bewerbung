from django.shortcuts import render
from .models import Skill

def index(request):
    skills = Skill.objects.all()
    context = {
        "skills": skills
        }
    return render(request, 'skills/index.html', context)