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
            print("Dados salvos:", form.cleaned_data)  # Para depuração
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('index')  # Redireciona para a URL 'index' após o envio
    else:
        form = ContactRequestForm()

    # Busca os itens do portfólio para passar ao template
    portfolio_items = PortfolioItem.objects.all()

    return render(request, 'OnePage/index.html', {
        'form': form,
        'portfolio_items': portfolio_items,  # Passando os itens do portfólio para o template
    })



def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'portfolio_items': portfolio_items})


def sobrenois(request):
    portfolio_items = PortfolioItem.objects.all()  # Obtém todos os itens do portfólio
    return render(request, 'OnePage/portfolio-details.html', {'portfolio_items': portfolio_items})


# def portfolio_details(request):
#     portfolio_items = PortfolioItem.objects.all()  # Pega todos os itens do portfólio
#     return render(request, 'portfolio_details.html', {'portfolio_items': portfolio_items})