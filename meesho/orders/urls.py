from django.conf.urls import url, include
from . import views



urlpatterns = [
	url(r'^place_order/?$', views.place_order, name="place_order"),
]
