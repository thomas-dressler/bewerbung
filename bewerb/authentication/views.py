from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('motivation')
        else:
            messages.success(request, ("Das hat leider nicht funktioniert... Username und Password korrekt eingegeben?"))
            return redirect('login')
    else:
        return render(request, 'authentication/index.html', {})
