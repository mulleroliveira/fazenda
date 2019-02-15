from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput
from . models import Animal, Fazendeiro

class AnimalForm(ModelForm):
      class Meta:
            model = Animal
            fields = ('__all__')
            widgets = {
                  'nome':TextInput(attrs={'class':'form-control'}),
                  'sexo':Select(attrs={'class':'form-control'}),
                  'raca':TextInput(attrs={'class':'form-control'}),
                  'cientifico':TextInput(attrs={'class':'form-control'}),
                  'peso':NumberInput(attrs={'class':'form-control'}),
                  'tamanho':NumberInput(attrs={'class':'form-control'}),
                  'expectativa':NumberInput(attrs={'class':'form-control'}),
                  'tipo_criacao':Select(attrs={'class':'form-control'})
            }

class FazendeiroForm(ModelForm):
      class Meta:
            model = Fazendeiro
            fields = ('__all__')
            widgets = {
                  'nome':TextInput(attrs={'class':'form-control'}),
                  'sexo':Select(attrs={'class':'form-control'}),
                  'data_nasc':DateInput(attrs={'class':'form-control'}),
                  'cpf':TextInput(attrs={'class':'form-control'}),
                  'rg':TextInput(attrs={'class':'form-control'}),
                  'funcao':TextInput(attrs={'class':'form-control'}),
                  'peso':NumberInput(attrs={'class':'form-control'}),
                  'altura':NumberInput(attrs={'class':'form-control'}),
                  'cidade':TextInput(attrs={'class':'form-control'}),
                  'estado':Select(attrs={'class':'form-control'}),
                  'salario':NumberInput(attrs={'class':'form-control'})
            }