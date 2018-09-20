from django.conf.urls import url
from .import views

urlpatterns = [
	
	url(r'^$', views.home, name='home'),	
	url(r'^list$', views.car_list, name='car_list'),
	url(r'^create$', views.create_list, name='create_list'),
	url(r'^models/(?P<id>[0-9]+)/$', views.model_list, name='model_list'),
	url(r'^models_detail/(?P<id>[0-9]+)/$', views.model_detail_list, name='model_detail_list'),
	url(r'^detail/(?P<id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^type/(?P<id>[0-9]+)/$', views.type_list, name='type_list'),
	url(r'^price-range$', views.price_range, name='price_range'),
	url(r'^results$', views.search, name='search'),

]