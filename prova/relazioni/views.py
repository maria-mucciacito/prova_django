from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Fly,Airport
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='/login/')
def selection_airport(request):
    ls_airports = Airport.objects.all()
    context = {'airports' : ls_airports}
    return render(request,'relazioni/form_prenotazione.html',context)

def visualizza_voli(request):
    ls_voli = []
    if request.method == 'POST':
        aeroporto_partenza = request.POST['a_partenza']
        aeroporto_arrivo = request.POST['a_arrivo']
        data = request.POST['data']

        ls_voli = Fly.objects.filter(Q(aeroporto_partenza=aeroporto_partenza) & Q(aeroporto_arrivo=aeroporto_arrivo) & Q(data_partenza=data))
        messages.success(request, 'Ecco tutti i voli disponibili')
        voli = []
        for index in ls_voli:
            volo = Fly.objects.get(code_volo=index)
            voli.append(volo)
        context = {
            'voli': voli,
        }

    else:
        messages.error(request, 'Non ci sono voli disponibili!')
    
    return render(request,'relazioni/voli.html',context)
    