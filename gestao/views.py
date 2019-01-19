from django.shortcuts import render
from . models import Animal

def home(request):
    return render(request, 'home.html')

def list_animais(request):
      animais = Animal.objects.all()
      return render(request, 'animal/list.html', {'animais':animais})