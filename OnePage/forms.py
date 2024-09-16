from django import forms
from .models import Mensagem

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ('Nome_Completo','Endereço_Email','Numero_de_telefone','mensagem')  # List the fields you want to include

    Nome_Completo = forms.CharField(
        label='Nome completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...'})
    )
    Endereço_Email = forms.EmailField(
        label='Endereço de Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
    )
    Numero_de_telefone = forms.CharField(
        label='Número de telefone',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(123) 456-7890'})
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...', 'style': 'height: 10rem'})
    )

#precisa ser ajustado 