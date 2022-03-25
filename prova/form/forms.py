from django.forms import ModelForm
from .models import Utente

class UtenteForm(ModelForm):
    
    class Meta:
        model = Utente
        fields = '__all__'