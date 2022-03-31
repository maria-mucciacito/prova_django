from django.shortcuts import render
from django.contrib import messages
from django.template import context
from .models import Utente
from .forms import UtenteForm


# Create your views here.
def posti(request):
    return render(request, 'form/posti.html')

def form(request):
    return render(request, 'form/index.html')

def insert_utente(request):
    context = {}
    if request.method == 'POST':
        form = UtenteForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Utente registrato')
        else:
            messages.error(request, 'Errore!')
        context = {'form': form}
    
    return render(request, 'form/index.html', context=context)

def visualizza_utenti(request):
    obj_ls = Utente.objects.all()
    context = {'obj':obj_ls}

    return render(request, 'form/index.html', context=context)

def delete_utente(request,pk):
    utente = Utente.objects.get(id=pk)
    if request.method == 'POST':
        utente.delete()
        messages.success(request, 'Utente eliminato')
    else:
        messages.error(request, 'Errore')
    context = {'item' : utente}
    return render(request, 'form/delete.html', context)

def update_utente(request,pk):
    utente = Utente.objects.get(id=pk)
    form = UtenteForm(instance=utente)
    if request.method == 'POST':
        form = UtenteForm(request.POST, instance=utente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utente aggiornato')
    context = {'form': form}
    return render(request, 'form/update.html', context)

