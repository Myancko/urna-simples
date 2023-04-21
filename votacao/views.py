from django.shortcuts import render
from .form import form_criar_elecao
from .models import eleicao

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def home (request):
    
    votacoes = eleicao.objects.all()
    
    return render (request, 'home.html', {'votacao':votacoes})

def criar_votacao  (request):

    form = form_criar_elecao()
    
    if request.method == "POST":
        
        form = form_criar_elecao(request.POST, request.FILES)
        if form.is_valid():

            #file_two = Aproveitamento_de_disciplina( comprovante = request.FILES['comprovante'])
            print('ok')
            form.save()
            return HttpResponseRedirect(reverse('Home'))
        else:
            
            print(form, '<<<<<<<')
            return render (request, 'criar_votacao.html', {'form':form})
        
    return render (request, 'criar_votacao.html', {'form':form})

def vote (request, id):
    
    votacao = eleicao.objects.get(id=id)
    
    if request.method == "POST":
        try:
            voto = request.POST
            print(voto, 'chegou')
            print(voto['voto'], 'aq  <<<')

            para_quem_foi_o_voto = User.objects.get(numero=voto['voto'])
            para_quem_foi_o_voto.total_de_votos += 1
            para_quem_foi_o_voto.save()
        except:
            
            return render (request, 'votar.html', {'votacao':votacao})
    
    return render (request, 'votar.html', {'votacao':votacao})