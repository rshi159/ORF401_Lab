from django.db import models
from django.core.validators import RegexValidator
import re
# Create your models here.

# https://stackoverflow.com/questions/59480134/how-to-store-a-phone-number-in-django-model
# error message when a wrong format entered
phone_message = 'Phone number must be entered in the format: 05999999999' 

 # your desired format 
phone_regex = RegexValidator(
    # regex=r^[-+]?[0-9]+$,
    regex = re.compile(r'\d+'),
    message=phone_message
)



class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  email = models.CharField(max_length=64)
  rating = models.IntegerField()
  # phone_number = models.IntegerField()
  # finally, your phone number field
  # phone_number = models.CharField(validators=[phone_regex], max_length=60)
  phone_number = models.CharField(max_length=60)
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
