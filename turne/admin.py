from django.contrib import admin
from turne.models import Cantor, Pais, Turne


class Cantores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'estilo')
    list_display_links = ('estilo',)
    search_fields = ('nome', 'estilo',)
    list_per_page = 10

admin.site.register(Cantor, Cantores)

class Paises(admin.ModelAdmin):
    list_display = ('pais', 'data_criacao', 'continente', 'populacao')
    list_display_links = ('pais','continente')
    search_fields = ('pais',)

admin.site.register(Pais, Paises)

class Turnes(admin.ModelAdmin):
    list_display = ('cantor', 'pais', 'modelo')
    list_display_links = ('cantor','modelo','pais')

admin.site.register(Turne, Turnes)