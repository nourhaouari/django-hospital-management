from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('dashboard')
            
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
