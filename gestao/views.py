from django.shortcuts import render, redirect
from . models import Animal, Fazendeiro
from datetime import datetime, timedelta
from . forms import AnimalForm, FazendeiroForm

def horario():
      data_e_hora_atuais = datetime.today() - timedelta(hours=3)
      if data_e_hora_atuais.hour >= 6 and data_e_hora_atuais.hour < 12:
            return 'Bom Dia!'
      elif data_e_hora_atuais.hour >= 12 and data_e_hora_atuais.hour < 18:
            return 'Boa Tarde!'
      else:
            return 'Boa Noite!'

def home(request):
      lista = []
      animais = Animal.objects.all()
      for c in animais[::-1]:
            if len(lista) == 3:
                  break
            else:
                  lista.append(c)
      return render(request, 'home.html', {'lista':lista, 'animal':lista[0], 'turno':horario()})

def animais_list(request):
      animais = Animal.objects.all()
      return render(request, 'animal/list.html', {'animais':animais})

def animal_show(request, animal_id):
      animal = Animal.objects.get(id=animal_id)
      return render(request, 'animal/show.html', {'animal':animal})

def animal_form(request):
      if request.method == 'POST':
            form = AnimalForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('/gestao/animais/')
            else:
                  return render(request, 'animal/form.html', {'form':form})
      else:
            form = AnimalForm()
            return render(request, 'animal/form.html', {'form':form})

def animal_edit(request, animal_id):
      if request.method == 'POST':
            animal = Animal.objects.get(pk=animal_id)
            form = AnimalForm(request.POST, instance=animal)
            if form.is_valid():
                  form.save()
                  return redirect('/gestao/animais/')
            else:
                  return render(request, 'animal/edit.html', {'form':form, 'animal_id':animal_id})
      else:      
            animal = Animal.objects.get(pk=animal_id)
            form = AnimalForm(instance=animal)
            return render(request, 'animal/edit.html', {'form':form, 'animal_id':animal_id})

def fazendeiros_list(request):
      fazendeiros = Fazendeiro.objects.all()
      return render(request, 'fazendeiro/list.html', {'fazendeiros':fazendeiros})

def fazendeiro_show(request, fazendeiro_id):
      fazendeiro = Fazendeiro.objects.get(id=fazendeiro_id)
      return render(request, 'fazendeiro/show.html', {'fazendeiro':fazendeiro})

def fazendeiro_form(request):
      if request.method == 'POST':
            form = FazendeiroForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('/gestao/fazendeiros/')
            else:
                  return render(request, 'fazendeiro/form.html', {'form':form})
      else:
            form = FazendeiroForm()
            return render(request, 'fazendeiro/form.html', {'form':form})

def fazendeiro_edit(request, fazendeiro_id):
      if request.method == 'POST':
            fazendeiro = Fazendeiro.objects.get(pk=fazendeiro_id)
            form = FazendeiroForm(request.POST, instance=fazendeiro)
            if form.is_valid():
                  form.save()
                  return redirect('/gestao/fazendeiros/')
            else:
                  return render(request, 'fazendeiro/edit.html', {'form':form, 'fazendeiro_id':fazendeiro_id})
      else:
            fazendeiro = Fazendeiro.objects.get(id=fazendeiro_id)
            form = FazendeiroForm(instance=fazendeiro)
            return render(request, 'fazendeiro/edit.html', {'form':form, 'fazendeiro_id':fazendeiro_id})