from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name="home"),
    path('index/', views.index, name="index"),
    path('properties/', views.properties, name="properties"),
    path('contact/', views.contact, name="contact"),
    path('propertyDetails/', views.propertyDetails, name="propertyDetails"),
    
    
]