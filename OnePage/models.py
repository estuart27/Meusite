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


class Media(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='media/fotos/')

    def __str__(self):
        return f"{self.nome}"
    

class Briefing(models.Model):
    TIPO_PROJETO_CHOICES = [
        ("site", "Desenvolvimento de Site"),
        ("chatbot", "Chatbot com IA"),
        ("google_negocio", "Consultoria Google Meu Negócio"),
        ("ifood", "Consultoria para iFood"),
        ("trafego", "Tráfego Pago"),
        ("redes", "Consultoria para Redes Sociais"),
        ("logo", "Criação de Logotipo"),
        ("outro", "Outro"),
    ]

    ORCAMENTO_CHOICES = [
        ("1000-1500", "R$1.000 a R$1.500"),
        ("1500-3000", "R$1.500 a R$3.000"),
        ("3000-6000", "R$3.000 a R$6.000"),
        ("sob_consulta", "A definir / Sob consulta"),
    ]

    PRAZO_CHOICES = [
        ("1-2", "1-2 semanas"),
        ("2-4", "2-4 semanas"),
        ("4-8", "4-8 semanas"),
        ("flexivel", "Prazo flexível"),
    ]

    EXPERIENCIA_CHOICES = [
        ("iniciante", "Sou iniciante, preciso de orientação"),
        ("intermediario", "Já tenho alguma experiência"),
        ("avancado", "Já participei de projetos semelhantes"),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)
    tipo_projeto = models.CharField(max_length=20, choices=TIPO_PROJETO_CHOICES)
    objetivo = models.TextField()
    funcionalidades = models.TextField(blank=True)
    referencias = models.TextField(blank=True)
    orcamento = models.CharField(max_length=20, choices=ORCAMENTO_CHOICES)
    prazo = models.CharField(max_length=20, choices=PRAZO_CHOICES)
    experiencia = models.CharField(max_length=20, choices=EXPERIENCIA_CHOICES)
    mensagem_final = models.TextField(blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Briefing'
        verbose_name_plural = 'Demandas'

    def __str__(self):
        return f"{self.nome} - {self.tipo_projeto}"
