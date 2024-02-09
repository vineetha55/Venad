from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_page(request):
    return render(request,"login_page.html")

def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect("/dashboard/")
    else:
        return redirect("/login_page/")

