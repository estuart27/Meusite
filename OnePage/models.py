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
        ('video', 'Vídeos'),  # Nova categoria para vídeos
        ('outros', 'Outros'),
    ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    project_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='portfolio/thumbnails/')
    link = models.URLField(max_length=200, blank=True, null=True)  # Campo para o link do projeto
    description = models.TextField(blank=True, null=True)
    completion_date = models.DateField(null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    
    # Novos campos para vídeos
    has_video = models.BooleanField(default=False)
    video_url = models.FileField(upload_to='portfolio/videos/', blank=True, null=True)
    
    # Campos opcionais para case study que estavam no template original
    case_study = models.BooleanField(default=False)
    case_study_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.project_name

