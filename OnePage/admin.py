from django.contrib import admin
from .models import Mensagem,PortfolioItem, Media, Briefing

@admin.register(Mensagem)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('Nome_Completo','Endereço_Email','Numero_de_telefone','mensagem')


admin.site.register(PortfolioItem)
admin.site.register(Media)
admin.site.register(Briefing)

