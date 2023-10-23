from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse


from typing import ContextManager
from .models import Passenger, flight

def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user
    }
    return redirect('home')

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})



def home(request):
    context = {
        "flights": flight.objects.all(),
        "user": request.user
    }
    return render(request, "index.html",context)

def flights(request, flight_id):
    try:
        f=flight.objects.get(pk=flight_id)
        context={
            "flight":f,
            "passengers":f.passengers.all(),
            "non_passengers":Passenger.objects.exclude(flights=f).all()
        }
        return render(request, "flight.html", context)
    except flight.DoesNotExist:
        raise Http404("Flight does not exist")
    
def book(request, flight_id):
    try:
        passenger_id=int(request.POST["passenger"])
        f=flight.objects.get(pk=flight_id)
        p=Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "error.html", {"message":"No selection."})
    except flight.DoesNotExist:
        return render(request, "error.html", {"message":"Flight not found - 404"})
    except Passenger.DoesNotExist:
        return render(request, "error.html", {"message":"Passenger not found - 404"})
    p.flights.add(f)
    return HttpResponseRedirect(reverse("flight", args=[flight_id]))