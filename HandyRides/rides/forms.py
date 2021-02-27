from django import forms


class RideForm(forms.Form):
  search_city = forms.CharField(label='Search City', max_length=64)#, required=False)
  search_state = forms.CharField(label='Search State', max_length=2)#, required=False)
