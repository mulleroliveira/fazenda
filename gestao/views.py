from django.shortcuts import render
from . models import Animal

def home(request):
      lista = []
      animais = Animal.objects.all()
      for c in animais[::-1]:
            if len(lista) == 3:
                  break
            elif c in lista:
                  pass
            else:
                  lista.append(c)
      return render(request, 'home.html', {'lista':lista})

def list_animais(request):
      animais = Animal.objects.all()
      return render(request, 'animal/list.html', {'animais':animais})