from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactRequestForm
from django.contrib import messages
from .models import PortfolioItem  # Importando o modelo de itens do portfólio


def index(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            print("Dados salvos:", form.cleaned_data)  # Adicione isso para depuração
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('index')  # Aqui, 'index' é o nome da URL para a view `index`
    else:
        form = ContactRequestForm()

    # Busca os itens do portfólio para passar ao template
    portfolio_items = PortfolioItem.objects.all()

    return render(request, 'OnePage/index.html', {
        'form': form,
        'portfolio_items': portfolio_items,  # Passando os itens do portfólio para o template
    })




def Sobre(request):
    return render(request, 'OnePage/SobreNois.html')


