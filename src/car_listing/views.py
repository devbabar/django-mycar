from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from .models import Car,Catagory,Make, Images, Model
from django.db.models import Q
from django.db.models import Count,Sum, Max, Min, Prefetch
from .forms import CarForm, ImageForm, PriceRangeForm
from django.forms import modelformset_factory
from django.core import serializers
from django.contrib import messages
import json

'''------------------------------------------
******************* Home ********************
------------------------------------------'''
def home(request):
	form = PriceRangeForm(request.POST or None)
	mycar = Car.objects.all().select_related('catagory','make','model').prefetch_related('img')
	home_display_list = mycar.order_by('-timestamp')[:6]
	if (len(home_display_list) > 3) and (len(home_display_list) < 6):
		home_display_list = home_display_list[:3]
	else:
		home_display_list = home_display_list[:6]
	car_type=mycar.values('catagory__catagory','catagory__id').annotate(Count('catagory'))
	car = mycar.values('make__make','make__id').annotate(Count('make'))
	context={
		'form':form,
		'car':car,
		'car_type':car_type,
		'mycar':mycar,
		'home_display_list':home_display_list
	}
	return render(request, 'car_listing/home.html',context)

'''------------------------------------------
******************* Search Bar **************
------------------------------------------'''
def search(request):
	
	result=Car.objects.all().select_related('catagory','make','model').prefetch_related('img')
	""" Note: For Search  """
	if 'q' in request.GET:
		query = request.GET['q']
		if not query or len(query) < 4:
			messages.error(request,"Sorry, you have entered an invalid search, please try again.")
			return HttpResponseRedirect('/mycar/')
		if query:
			result=result.filter(
				Q(price__icontains=query)|
				Q(model__model__icontains=query)|
				Q(make__make__icontains=query)|
				Q(catagory__catagory__icontains=query)|
				Q(year__icontains=query)
				).distinct()

	""" Note: For page pagination """
	paginator = Paginator(result, 3) # Show 3 post per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context={
		'result':queryset
	}
	return render(request, 'car_listing/search_results.html', context)

'''------------------------------------------
*************** Main listing page ***********
------------------------------------------'''
"""Note: we used ('catagory__catagory') to get the catagory name instead of getting id 
	mycar.values('catagory__catagory').annotate(Count('catagory')) to get the count for each catagory name"""

def car_list(request):
	
	form = PriceRangeForm(request.POST or None)

	mycar = Car.objects.all().select_related('catagory','make','model').prefetch_related('img')
	published=mycar.order_by('-timestamp')
	car_type = mycar.values('catagory__catagory','catagory__id').annotate(Count('catagory'))
	car = mycar.values('make__make','make__id').annotate(Count('make'))

	""" Note: For page pagination """
	paginator = Paginator(published, 2) # Show 3 post per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context={
		'form':form,
		'car':car,
		'car_type':car_type,
		'mycar':mycar,
		'published':queryset
	}
	return render(request, 'car_listing/car_list.html',context)


'''------------------------------------------
************* Create New List ***************
------------------------------------------'''
def create_list(request,*args, **kwargs):
	ImageFormset = modelformset_factory(Images,form=ImageForm,extra=3)	
	if request.method == 'POST':
		form=CarForm(request.POST)
		formset=ImageFormset(request.POST,request.FILES,queryset=Images.objects.none())
		
		if form.is_valid() and formset.is_valid():
			
			catagory= form.cleaned_data['catagory']
			catagory, created = Catagory.objects.get_or_create(catagory=catagory)

			make = form.cleaned_data['make']
			make, created = Make.objects.get_or_create(make=make)
			
			model = form.cleaned_data['model']
			model, created = Model.objects.get_or_create(model=model)
			
			year = form.cleaned_data['year']
			price = form.cleaned_data['price']
			mileage = form.cleaned_data['mileage']
			street = form.cleaned_data['street']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			contact = form.cleaned_data['contact']
			contact_name = form.cleaned_data['contact_name']
			result = Car.objects.create(catagory=catagory,make=make,model=model,year=year,price=price,mileage=mileage,street=street,city=city,state=state,contact=contact,contact_name=contact_name)
			for i in formset.cleaned_data:
				image=i['image']
				image=Images.objects.create(car=result,image=image,make=make,model=model)

			return HttpResponseRedirect('/mycar/list')
	else:		
		form=CarForm()
		formset = ImageFormset(queryset=Images.objects.none())
	return render(request, 'car_listing/create_list.html',{'form':form,'formset':formset})


'''------------------------------------------
************* Model list for Ajax ***********
------------------------------------------'''
def model_list(request,id):
	
	model_list = Images.objects.values('model__model','model__id').annotate(Count('car',distinct=True)).filter(make_id=id)
	return JsonResponse(list(model_list),safe=False)


'''------------------------------------------
*************** Car by Type *****************
------------------------------------------'''
def type_list(request,id):
	
	type_list= Car.objects.filter(catagory_id=id).select_related('catagory','make','model').prefetch_related('img')

	context = {
		'type_list':type_list
	}
	return render(request, 'car_listing/type_list.html',context)


'''------------------------------------------
******* Expand model list in Detail *********
------------------------------------------'''
def model_detail_list(request,id):

	car_model = Car.objects.filter(model_id=id).select_related('catagory','make','model').prefetch_related('img')
	context = {

		'car_model':car_model
	}
	return render(request,'car_listing/model_detail_list.html',context)


'''------------------------------------------
************ Detail individual car **********
------------------------------------------'''
def detail(request,id):
	
	car_mod = get_object_or_404(Car.objects.select_related('catagory','make','model').prefetch_related('img'),id=id)
	context = {
		
		'car_mod':car_mod
	}
	return render(request, 'car_listing/detail.html',context)


'''------------------------------------------
********* Price range search ****************
------------------------------------------'''
def price_range(request):
	form = PriceRangeForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			# min_price=request.GET.get('min_price')
			min_price=form.cleaned_data['minprice']
			max_price=form.cleaned_data['maxprice']		
			
			test = Car.objects.all().select_related('catagory','make','model').prefetch_related('img')
			price_range=test.filter(price__range = (min_price, max_price))

			context = {
				'form':form,
				'price_range':price_range
			}
			return render(request, 'car_listing/price_range.html',context)
	else:
		form = PriceRangeForm()
	return render(request, 'car_listing/price_range.html',context)
