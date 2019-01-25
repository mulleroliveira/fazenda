from django.shortcuts import render
from . models import Animal, Fazendeiro
from datetime import datetime, timedelta

data_e_hora_atuais = datetime.today() - timedelta(hours=3)
#A localização de onde o Python pega o horário eu não sei, mas ví que a diferença do horário de onde é pegado, tem 3
#horas adiatada comparada com o horário daqui do Brasil. Logo, só precisamos diminuir 3 horas pra ficar "correto".

def horario():
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

def list_animais(request):
      animais = Animal.objects.all()
      return render(request, 'animal/list.html', {'animais':animais})

def show_animal(request, animal_id):
      animal = Animal.objects.get(id=animal_id)
      return render(request, 'animal/show.html', {'animal':animal})

def list_fazendeiros(request):
      fazendeiros = Fazendeiro.objects.all()
      return render(request, 'fazendeiro/list.html', {'fazendeiros':fazendeiros})

def show_fazendeiro(request, fazendeiro_id):
      fazendeiro = Fazendeiro.objects.get(id=fazendeiro_id)
      return render(request, 'fazendeiro/show.html', {'fazendeiro':fazendeiro})