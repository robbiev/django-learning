# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.utils import timezone

from app1.models import Reservation

class ReservationForm(ModelForm):
  class Meta:
    model = Reservation 
    exclude = ['at']

def index(request):
  reservations = Reservation.objects.all()
  return render(request, 'app1/index.html', {'todays_reservations':reservations})

def new_reservation(request):
  return render(request, 'app1/new_reservation.html', {'form': ReservationForm()})

def save_reservation(request):
  #return HttpResponse(request.POST['meh']) 
  form = ReservationForm(request.POST)
  reservation = form.save(commit=False)
  reservation.at = timezone.now()
  reservation.save()

  return HttpResponseRedirect(reverse('app1:index'))

def not_found(request):
  return render(request, '404.html', {}, status=404)
