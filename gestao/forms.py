from django.forms import ModelForm, TextInput, NumberInput, Select
from . models import Animal

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