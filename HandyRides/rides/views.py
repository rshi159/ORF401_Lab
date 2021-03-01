from django.shortcuts import render, redirect

from .models import Person

# relative import of forms
from .forms import RideForm, NewRideForm
# Create your views here.


def index(request):
# make a dict named context
  context = {}
# check requests and filter.
  if "search_state" in request.GET:
    search = request.GET["search_state"]

    context["people"] = Person.objects.filter(
        origination_state__icontains=search) | Person.objects.filter(destination_state__icontains=search) | Person.objects.filter(destination_city__icontains=search)
  
  if "search_city" in request.GET:
    search = request.GET["search_city"]

    context["people"] = context["people"].filter(
        origination_city__icontains=search) | Person.objects.filter(destination_state__icontains=search) | Person.objects.filter(destination_city__icontains=search)
  	
  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  # context has items "people", "form", "new_ride_form"
  # people = the search results
  # form is 
  # new_ride_form =

  # https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/
  # render function is a django shortcut.
  # takes arguments request, templatename, and context
  # returns a httpresponse object with the rendered text.

  # request is The request object used to generate this response.
  # template is the full name of a template to use or sequence of template names
  # context is A dictionary of values to add to the template context.
  return render(request, "index_view.html", context)

def create(request):
  # if request.method == "POST":
  #   new_ride = NewRideForm(request.POST)
  #   new_ride.save()
  # Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.
  return redirect("/rides")
