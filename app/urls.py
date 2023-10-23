from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),


    path("home/",views.home, name="home"),
    path("<int:flight_id>", views.flights, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]