from django.shortcuts import render

from .models import Person

# relative import of forms
from .forms import RideForm, NewRideForm
# Create your views here.


def index(request):

  context = {}
  if "search_state" in request.GET:
    search = request.GET["search_state"]

    context["people"] = Person.objects.filter(
        origination__icontains=search) | Person.objects.filter(destination_state__icontains=search) | Person.objects.filter(destination_city__icontains=search)
  
  if "search_city" in request.GET:
    search = request.GET["search_city"]

    context["people"] = context["people"].filter(
        origination__icontains=search) | Person.objects.filter(destination_state__icontains=search) | Person.objects.filter(destination_city__icontains=search)
  	
  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  return render(request, "index_view.html", context)

def create(request):
  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()

  return redirect("/rides")
