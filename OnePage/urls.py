# OnePage/urls.py

from django.urls import path
from . import views  # Importe as views que você irá usar

urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de URL para a view 'home'
    path('SobreNois', views.Sobre, name='SobreNois'),  # Exemplo de URL para a view 'home'


    # Adicione outras URLs conforme necessário
]

