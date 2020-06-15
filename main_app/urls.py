from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('test/', views.test, name='test'),
path('about/', views.about, name='about'),
path('dogs/', views.dogs_index, name='index')
]