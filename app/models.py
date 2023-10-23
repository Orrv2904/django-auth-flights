from django.db import models

class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} - {self.city}"

class flight(models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id} - From {self.origin} to {self.destination}"
    
class Passenger(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    flights = models.ManyToManyField(flight,blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"