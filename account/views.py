from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User

def account_signup(req):
    if req.method == "POST":
        name = req.POST.get("name", "")
        email = req.POST.get("email", "")
        password = req.POST.get("password", "")
        password2 = req.POST.get("password2", "")

        if name and email and password and password2 and (password == password2):
            user = User.objects.create_user(name, email, password)
            print("all good", user)
            return redirect("/account/login")
        else:
            print("error in form")
    else:
        print("form is empty")
    return render(req, "account/signup.html")


def account_login(req):
    if req.method == "POST":
        email = req.POST.get("email", "")
        password = req.POST.get("password", "")

        if email and password:
            user = authenticate(req, email=email, password=password)

            if user is not None:
                login(req, user)
                return redirect("/")

    return render(req, "account/login.html")
