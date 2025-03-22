from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactRequestForm
from django.contrib import messages
from .models import PortfolioItem  # Importando o modelo de itens do portfólio
# from .utils import analizar_partida  # Certifique-se de que a função resposta_bot está no arquivo correto;



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
    # Filtrar apenas os itens de portfólio que são vídeos ou têm has_video=True
    video_items = PortfolioItem.objects.filter(has_video=True) | PortfolioItem.objects.filter(category='video')

    # feedback = analizar_partida() #IA em desenvolvimento
    
    context = {
        'video_items': video_items,
        'portfolio_items': portfolio_items,
    }
    return render(request, 'seu_template.html', context)


def sobrenois(request):
    portfolio_items = PortfolioItem.objects.all()  # Obtém todos os itens do portfólio
    return render(request, 'OnePage/portfolio-details.html', {'portfolio_items': portfolio_items})



import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import responder_com_pdf

logger = logging.getLogger(__name__)

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



# def portfolio_details(request):
#     portfolio_items = PortfolioItem.objects.all()  # Pega todos os itens do portfólio
#     return render(request, 'portfolio_details.html', {'portfolio_items': portfolio_items})