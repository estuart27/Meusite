from django.db import models

class Mensagem(models.Model):
    Nome_Completo = models.CharField(max_length=255)
    Endereço_Email = models.EmailField()
    Numero_de_telefone = models.CharField(max_length=20)
    mensagem = models.TextField()

    def __str__(self):
        return f"{self.Nome_Completo} - {self.Endereço_Email}"

class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('e-commerce', 'E-commerce'),
        ('blog', 'Blog'),
        ('onepage', 'OnePage'),
        ('landing page', 'Landing Page'),
        ('outros', 'Outros'),
    ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    project_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/')
    link = models.URLField(max_length=200, blank=True, null=True)  # Adicionando o campo para o link do projeto

    def __str__(self):
        return self.project_name

