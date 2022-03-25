from django.db import models

# Create your models here.
class Utente(models.Model):
 
    email = models.EmailField(max_length=100, null=False)
    nome = models.CharField(max_length=200, null=False)
    cognome = models.CharField(max_length=200, null=False, default='Rossi')
    
    def __str__(self):
        return self.nome