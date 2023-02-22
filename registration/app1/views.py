from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Capteurs, Actionneur
from datetime import datetime
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("check your password!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def create_capteurs(request):
    capteurs = Capteurs.objects.create(
        temperature=25.5, humidite=60.0, courant=2.5, luminosite=2500)
    return render(request, 'create_capteurs.html', {'capteurs': capteurs})


def create_actionneur(request):
    actionneur = Actionneur.objects.create(
        regulateur_charge='Type A', date_mesure=datetime.now())
    return render(request, 'create_actionneur.html', {'actionneur': actionneur})
