from django import forms
from car_listing.choices import *
from .models import Car,Catagory,Images

year_choice		=[('','Select Year')]
year_choice.extend([((year),(year)) for year in range(1990, 2019)])


class CarForm(forms.Form):

	'''Note: for bootstrap we use widget to add up attribute class'''
	catagory = forms.ChoiceField(choices=catagory_choice, widget=forms.Select(attrs={'class':'form-control',}))
	make = forms.ChoiceField(choices=make_choice, widget=forms.Select(attrs={'class':'form-control',}))
	model = forms.ChoiceField(choices=model_choice, widget=forms.Select(attrs={'class':'form-control',}))
	year = forms.ChoiceField(choices=year_choice, widget=forms.Select(attrs={'class':'form-control',}))
	price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.TextInput(attrs={'class':'form-control',}))
	mileage = forms.IntegerField(max_value=None,min_value=None, widget=forms.TextInput(attrs={'class':'form-control',}))
	street = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control',}))
	city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control',}))
	state = forms.ChoiceField(choices=state_choice, widget=forms.Select(attrs={'class':'form-control',}))
	contact = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class':'form-control',}))
	contact_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control',}))

class ImageForm(forms.ModelForm):
	image=forms.ImageField(label='Image')
	class Meta:
		model = Images
		fields=('image',)


class PriceRangeForm(forms.Form):
	minprice = forms.DecimalField(max_digits=8, decimal_places=2)
	maxprice = forms.DecimalField(max_digits=8, decimal_places=2)
