from django.shortcuts import render
from .models import Reference
# Create your views here.

def index(request):
    ref = Reference.objects.all()
    context = {
        "refs": ref
        }
    return render(request, 'references/index.html', context)