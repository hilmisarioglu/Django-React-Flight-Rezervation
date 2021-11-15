from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length=100)
    operatingAirlines = models.CharField(max_length=100)
    departureCity = models.CharField(max_length=100)
    dateOfDeparture = models.DateField(auto_now_add=True)
    estimatedTimeOfDeparture = models.CharField(max_length=100)
    
    def __str__(self):
        return self.flightNumber
    
class Passenger(models.Model):
    flight = models.ForeignKey(Flight , on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.firstName
        

class Reservation(models.Model):
    flight = models.ForeignKey(Flight , on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.passenger)

    