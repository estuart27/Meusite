# OnePage/urls.py

from django.urls import path
from . import views  # Importe as views que você irá usar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de URL para a view 'home'
    path('sobrenois', views.sobrenois, name='sobrenois'),  # Exemplo de URL para a view 'home'
    path('api/chat/', views.chat_api, name='chat_api'),  # API do chat


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)