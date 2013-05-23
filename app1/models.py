from django.db import models

class Employee(models.Model):
  name = models.CharField(max_length=50)
  def __unicode__(self):
    return self.name 

class Product(models.Model):
  name = models.CharField(max_length=50)
  def __unicode__(self):
    return self.name 

class Reservation(models.Model):
  choice = models.ForeignKey(Product) 
  at = models.DateField()
  who = models.ForeignKey(Employee)

  def __unicode__(self):
    return '%s ordered %s at %s' % (self.who, self.choice, str(at))

# Create your models here.
