from django.db import models
from phone_field import PhoneField

# Create your models here.
class Add_guide(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    language = models.CharField(max_length=500)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Add_hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pin = models.IntegerField()
    country = models.CharField(max_length=200)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    star = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Add_package(models.Model):
    name = models.CharField(max_length=200)
    rate = models.IntegerField()
    details = models.TextField()

    def __str__(self):
        return self.name

class Add_place(models.Model):
    source = models.CharField(max_length=200)  
    destination = models.CharField(max_length=200)       
    bus_distance = models.IntegerField()
    train_distance = models.IntegerField()
    flight_distance = models.IntegerField()
    bus_fare = models.IntegerField()
    train_fare = models.IntegerField()
    flight_fare = models.IntegerField() 
    bus_duration = models.IntegerField() 
    train_duration = models.IntegerField()
    flight_duration = models.IntegerField()
    visiting_places = models.TextField()

    def __str__ (self):
        return self.source + " to " + self.destination

