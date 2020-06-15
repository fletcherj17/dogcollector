from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def test(request):
    return HttpResponse('<h1>Test</h1>')

def about(request):
    return render(request, 'about.html')


# Add the Dog class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
Dog('Lolo', 'tabby', 'foul little demon', 3),
Dog('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
Dog('Raven', 'black tripod', '3 legged dog', 4)
]

def dogs_index(request):
    context = {'dogs': dogs}
    return render(request, 'dogs/index.html', context)