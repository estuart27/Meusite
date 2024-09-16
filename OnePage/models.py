from django.db import models

class Mensagem(models.Model):
    Nome_Completo = models.CharField(max_length=255)
    Endereço_Email = models.EmailField()
    Numero_de_telefone = models.CharField(max_length=20)
    mensagem = models.TextField()

    def __str__(self):
        return f"{self.Nome_Completo} - {self.Endereço_Email}"

# models.py
from django.db import models

class PortfolioItem(models.Model):
    category = models.CharField(max_length=100)
    project_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/')

    def __str__(self):
        return self.project_name
