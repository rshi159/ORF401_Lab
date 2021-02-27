from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  email = models.CharField(max_length=64)
  rating = models.IntegerField()
  phone_number = models.IntegerField()
  origination_address = models.CharField(max_length=64)
  origination_city = models.CharField(max_length=64)
  origination_state = models.CharField(max_length=2)
  destination_address = models.CharField(max_length=64)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
  vehicle_model = models.CharField(max_length=64)