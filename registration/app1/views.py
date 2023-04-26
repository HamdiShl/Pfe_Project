from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TemperatureData, HumidityData, LightData


# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def acceuilPage(request):
    return render(request, 'acceuil.html')

def dashboard(request):
    # Include primary key field in raw queries
    latest_temperature = TemperatureData.objects.using('default').raw('SELECT id, temperature FROM sensor_app_sensordata ORDER BY timestamp DESC LIMIT 1')
    latest_humidity = HumidityData.objects.using('default').raw('SELECT id, humidity FROM sensor_app_sensordata ORDER BY timestamp DESC LIMIT 1')
    latest_light = LightData.objects.using('default').raw('SELECT id, light_level FROM light_data ORDER BY timestamp DESC LIMIT 1')
    
    # Extract the values from RawQuerySet objects
    latest_temperature_value = next(iter(latest_temperature)).temperature
    latest_humidity_value = next(iter(latest_humidity)).humidity
    latest_light_value = next(iter(latest_light)).light_level
    
    # pass the extracted values to the template context
    context = {
        'latest_temperature': latest_temperature_value,
        'latest_humidity': latest_humidity_value,
        'latest_light': latest_light_value,
    }
    return render(request,'dashboard.html', context)





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






