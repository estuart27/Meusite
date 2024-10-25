from django import forms
from .models import Mensagem


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


