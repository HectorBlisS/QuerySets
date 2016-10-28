from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^cines/$', views.Cines.as_view(),name="cines"),
	url(r'^$',views.Home.as_view(),name="home"),

]