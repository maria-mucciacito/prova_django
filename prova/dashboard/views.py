from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import context 

from relazioni.models import *
# Create your views here.

'''def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login corretto!')
            return redirect('selection_airport')
        else:
            messages.info(request, 'Username o Password errati!')
    
    context = {}
    return render(request,'dashboard/login.html',context)'''

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def visualizza_voli(request):
    obj_ls = Fly.objects.all()
    context = {'voli':obj_ls}
    return render(request, 'dashboard/voli.html', context=context)

