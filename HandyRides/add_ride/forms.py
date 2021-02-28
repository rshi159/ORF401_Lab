from django import forms
from rides.models import Person


class RideForm(forms.Form):
  search_city = forms.CharField(label='search_city', max_length=64, required=False)
  search_state = forms.CharField(label='search_state', max_length=64, required=False)

# https://docs.djangoproject.com/en/3.0/topics/db/models/#meta-options
# Model metadata is “anything that’s not a field”,
class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    # fields = ['first_name','phone_number']
    exclude = []
