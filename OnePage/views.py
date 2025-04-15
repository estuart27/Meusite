from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import responder_com_pdf
from .forms import ContactRequestForm,BriefingForm
from .models import PortfolioItem,Media
import logging
import json


logger = logging.getLogger(__name__)

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

    portfolio_items = PortfolioItem.objects.all()

    return render(request, 'OnePage/index.html', {
        'form': form,
        'portfolio_items': portfolio_items,  # Passando os itens do portfólio para o template
    })


def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    # Filtrar apenas os itens de portfólio que são vídeos ou têm has_video=True
    video_items = PortfolioItem.objects.filter(has_video=True) | PortfolioItem.objects.filter(category='video')
    
    context = {
        'video_items': video_items,
        'portfolio_items': portfolio_items,
    }
    return render(request, 'seu_template.html', context)


def sobrenois(request):
    portfolio_items = PortfolioItem.objects.all()  # Obtém todos os itens do portfólio
    return render(request, 'OnePage/portfolio-details.html', {'portfolio_items': portfolio_items})


@csrf_exempt
def chat_api(request):
    logger.info("Requisição recebida para chat_api")
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            logger.info(f"Mensagem recebida: {user_message}")

            if not user_message:
                logger.warning("Mensagem vazia recebida")
                return JsonResponse({"error": "Mensagem vazia"}, status=400)

            logger.info("Processando com responder_com_pdf")
            resposta = responder_com_pdf(user_message)
            logger.info("Resposta gerada com sucesso")
            
            return JsonResponse({"response": resposta})
        except Exception as e:
            logger.error(f"Erro ao processar mensagem: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    logger.warning("Método não permitido")
    return JsonResponse({"error": "Método não permitido"}, status=405)


def consultorias(request):
    media_items = Media.objects.all()  # Obtém todos os itens do portfólio
    return render(request, 'OnePage/consultorias.html', {'media_items': media_items})



def formulario_projeto(request):
    if request.method == "POST":
        form = BriefingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return render(request, "OnePage/formulario_sucesso.html")  # página de sucesso
    else:
        form = BriefingForm()
    
    return render(request, "OnePage/formulario.html", {"form": form})

