# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from app1.models import Reservation

class ReservationForm(ModelForm):
  class Meta:
    model = Reservation 

def index(request):
  reservations = Reservation.objects.all()
  return render(request, 'app1/index.html', {'todays_reservations':reservations})

def new_reservation(request):
  return render(request, 'app1/new_reservation.html', {'form': ReservationForm()})

def save_reservation(request):
  #return HttpResponse(request.POST['meh']) 
  return HttpResponseRedirect(reverse('app1:index'))

def not_found(request):
  return render(request, '404.html', {}, status=404)
