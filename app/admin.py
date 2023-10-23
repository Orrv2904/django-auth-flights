from django.contrib import admin
from .models import *
# Register your models here.

class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1
    
class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]
    
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    

admin.site.register(Airport)
admin.site.register(flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)