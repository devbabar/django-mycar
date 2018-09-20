from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
import datetime

make_choice     =(('toyota','Toyota'),
				  ('nissan','Nissan'),
				  ('ford','Ford'),
				  ('chevrolet','Chevrolet'),
				  ('bmw','BMW'),
				  ('audi','Audi'),
				  ('acura','Acura'),
				  ('dodge','Dodge'),
				  ('jaguar','Jaguar'),
				  ('mercedes','Mercedes'),
				  )

class Catagory(models.Model):
	catagory = models.CharField(max_length=100)

	def __unicode__(self):
		return str(self.catagory)

class Make(models.Model):
	make = models.CharField(max_length=100)

	def __unicode__(self):
		return str(self.make)

class Model(models.Model):
	model = models.CharField(max_length=100)

	def __unicode__(self):
		return str(self.model)

class Car(models.Model):
	catagory 		= models.ForeignKey(Catagory)
	make 			= models.ForeignKey(Make)
	model 			= models.ForeignKey(Model)
	year			= models.IntegerField()
	price			= models.DecimalField(max_digits=8, decimal_places=2)
	mileage			= models.IntegerField()
	street			= models.CharField(max_length=150)
	city			= models.CharField(max_length=100)
	state			= models.CharField(max_length=100)
	contact			= models.CharField(max_length=12)
	contact_name	= models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True, null =True)

	def __unicode__(self):
		return str(self.make)

def get_image_filename(instance,filename):
	make=instance.car.make
	return "post_images/%s"%(filename)


class Images(models.Model):
	car = models.ForeignKey(Car,related_name='img', default=None)
	make = models.ForeignKey(Make)
	model = models.ForeignKey(Model)
	image = models.ImageField(upload_to=get_image_filename,verbose_name='Image',)

	def __unicode__(self):
		return str(self.image)
