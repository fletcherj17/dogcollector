from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def test(request):
    return HttpResponse('<h1>Test</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    context = {'dogs': dogs}
    return render(request, 'dogs/index.html', context)

def details (request, dog_id):
    dog = Dog.objects.get(id = dog_id)
    context = {'dog': dog}
    return render(request, 'dogs/details.html', context)