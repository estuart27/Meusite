from django import forms
from .models import Mensagem, Briefing


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['Nome_Completo', 'Endereço_Email', 'Numero_de_telefone', 'mensagem']
        widgets = {
            'Nome_Completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'Endereço_Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'Numero_de_telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 6}),
        }


from django import forms
from .models import Briefing

class BriefingForm(forms.ModelForm):
    nome = forms.CharField(label="Seu nome", max_length=100)
    email = forms.EmailField(label="Seu e-mail")
    whatsapp = forms.CharField(label="WhatsApp", max_length=20, required=False)

    tipo_projeto = forms.ChoiceField(
        label="Tipo de projeto",
        choices=[
            ("site", "Desenvolvimento de Site"),
            ("chatbot", "Chatbot com IA"),
            ("google_negocio", "Consultoria Google Meu Negócio"),
            ("ifood", "Consultoria para iFood"),
            ("trafego", "Tráfego Pago"),
            ("redes", "Consultoria para Redes Sociais"),
            ("logo", "Criação de Logotipo"),
            ("outro", "Outro"),
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )

    objetivo = forms.CharField(
        label="Qual o objetivo do seu projeto?",
        widget=forms.Textarea(attrs={"rows": 3}),
        help_text="Conte-nos o que você espera alcançar com esse projeto."
    )

    funcionalidades = forms.CharField(
        label="Funcionalidades desejadas",
        widget=forms.Textarea(attrs={"rows": 3}),
        help_text="Ex: Área de login, formulário de contato, blog, chatbot, etc.",
        required=False
    )

    referencias = forms.CharField(
        label="Tem referências ou inspirações?",
        widget=forms.Textarea(attrs={"rows": 2}),
        help_text="Links de sites que você gosta ou algo que te inspire",
        required=False
    )

    orcamento = forms.ChoiceField(
        label="Faixa de orçamento disponível",
        choices=[
            ("1000-1500", "R$1.000 a R$1.500"),
            ("1500-3000", "R$1.500 a R$3.000"),
            ("3000-6000", "R$3.000 a R$6.000"),
            ("sob_consulta", "A definir / Sob consulta")
        ]
    )

    prazo = forms.ChoiceField(
        label="Urgência do projeto",
        choices=[
            ("1-2", "1-2 semanas"),
            ("2-4", "2-4 semanas"),
            ("4-8", "4-8 semanas"),
            ("flexivel", "Prazo flexível")
        ]
    )

    experiencia = forms.ChoiceField(
        label="Qual o seu nível de familiaridade com projetos digitais?",
        choices=[
            ("iniciante", "Sou iniciante, preciso de orientação"),
            ("intermediario", "Já tenho alguma experiência"),
            ("avancado", "Já participei de projetos semelhantes")
        ]
    )

    arquivos = forms.FileField(
        label="Deseja anexar algum arquivo (ex: logo, briefing, ideias)?",
        required=False,
        widget=forms.ClearableFileInput()
    )

    mensagem_final = forms.CharField(
        label="Algo mais que gostaria de nos contar?",
        widget=forms.Textarea(attrs={"rows": 2}),
        required=False
    )

    class Meta:
        model = Briefing
        fields = '__all__'
