from django import forms
from django.forms import ModelForm
from .models import eleicao

class form_criar_elecao (ModelForm):
    
    class Meta:
        model = eleicao
        fields =  'nome', 'descricao', 'fim', 'participantes', 'foto'