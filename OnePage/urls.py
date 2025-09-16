# OnePage/urls.py

from django.urls import path
from . import views  # Importe as views que você irá usar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de URL para a view 'home'
    path('sobrenois', views.sobrenois, name='sobrenois'),  # Exemplo de URL para a view 'home'
    path('api/chat/', views.chat_api, name='chat_api'),  # API do chat
    path('consultorias/',views.consultorias, name='consultoria'),  
    path('seuprojeto/', views.formulario_projeto, name='formulario'),  # Exemplo de URL para a view 'home'
    path('servicos/chatbot',views.detalhes_chatbot,name='detalhes_chatbot'),
    path('servicos/agentes',views.detalhes_agentes,name='detalhes_agentes'),
    path('servicos/sites-onepage',views.detalhes_site_onepage,name='detalhes_site_onepage'),
    path('servicos/consultoria',views.detalhes_consultoria,name='detalhes_consultoria'),
    path('servicos/negocios',views.detalhes_negocio,name='detalhes_negocio'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)