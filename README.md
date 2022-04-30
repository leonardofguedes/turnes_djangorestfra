# CRIANDO API COM DJANGO REST FRAMEWORK EM 19 PASSOS 

e integrando em banco de dados no Pycharm (para iniciantes)

### 📋 Pycharm, Python, Django Rest Framework


1. No terminal do Pycharm instale o DRF | ele fará a API

```
    pip install DjangoRestFramework
```


2. No terminal do Pycharm, inicie o projeto. Obs1: Não esqueça o ponto. Obs2: Nesse modelo, o 'name' é setup.

```
    django-admin startproject name .
```


3. No terminal do Pycharm, inicie o app. Neste exemplo, 'name' será turne.

```
    django-admin startapp name
```


4. No terminal do Pycharm, instale o markdown. É o suporte do browser.

```
    pip install markdown
```


5. Em settings.py, na lista appinstaled, insira os novos apps ‘rest_framework’ e ‘turne’.


# CRIANDO MODELO


6. Em models.py, importe <models> de <django.db>. Ele pode já estar na idle. 

```
    from django.db import models
```


7. Crie a class/modelo:

```
    class Cantor(models.Model):
        nome = models.CharField(max_length=25)
        estilo = models.CharField(max_length=15)

        def __str__(self):
            return self.nome

    class Pais(models.Model):
        Cont = (
            ('O', 'Oceania'),
            ('A', 'America'),
            ('E', 'Europa'),
            ('F', 'Africa'),
            ('S', 'Asia'),
            ('U', 'Unknow')
        )

        nome = models.CharField(max_length=20)
        data_criacao = models.DateField()
        continente = models.CharField(max_length=1, choices=Cont, blank=False, null=False, default='U')
        populacao = models.CharField(max_length=12)

        def __str__(self):
            return self.nome
```

    
```
Informações:
Informação 1! No nível, observar a função max_lenght, choices, blank e null. 
Informação 2! O max_lenght de 1 caracter diz que no DB será salvo apenas 1 letras.
Informação 3! O choices aplica as variáveis dispostas.
Informação 4! O blank False não permite que no DB não tenha nível.
Informação 5! O null False não permite que seja nulo.
Informação 6! O Default é o modelo-base, que no caso escolhido é ‘B’.
```
    
8. Suba as migrações no Data Base através do terminal:

```
    python manage.py makemigrations
    python manage.py migrate
```
    
# CONFIGURAR O ADMIN

9. Em admin.py:

```    
    from django.contrib import admin
    from turne.models import Cantor, Pais
```
    
10. Criar a class que define os campos que serão mostrados ao admin:
```
    class Cantores(admin.ModelAdmin):
        list_display = ('id', 'nome', 'estilo')
        list_display_links = ('estilo',)
        search_fields = ('nome', 'estilo',)
        list_per_page = 10

    admin.site.register(Cantor, Cantores)

    class Paises(admin.ModelAdmin):
        list_display = ('nome', 'data_criacao', 'continente', 'populacao')
        list_display_links = ('nome','continente')
        search_fields = ('nome',)

    admin.site.register(Pais, Paises)
```
```
INFORMAÇÕES:
Informação 1! O ‘id’ sempre é gerado.
Informação 2! list_diplay_links são os Fields que o admin pode alterar/editar
Informação 3! search_fields serve para buscar os atributos indicados
Informação 4! list_per_page é o máximo de itens por página 
Informação 5! admin.site.register(m, c) registra o (modelo e a configuração)
```
    
11. Criar SuperUsuario no terminal:
```
    python manage.py createsuperuser
```
    
# CONFIGURAR SERIALIZER

12. Criar no app/package (Turne) o arquivo serializer.py

13. Dentro do arquivo, importar:
    
```
    from rest_framework import serializers
    from turne.models import Cantor, Pais
```
    
14. Criar a classe onde serão definidos modelos e campos a serem recebidos pela API.
    
```
    class CantorSerializer(serializers.ModelSerializer):
        class Meta: #qual o modelo e os campos que utilizaremos
            model = Cantor
            fields = '__all__'

    class PaisSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pais
            fields = ['nome', 'continente', 'populacao', 'data_criacao']
```
    
# CONFIGURAR VIEWS | Será onde os dados serão selecionados, definidos, recebidos

15. Em views.py import:
    
```  
    from rest_framework import viewsets
    from turne.models import Cantor, Pais
    from turne.serializer import CantorSerializer, PaisSerializer
```
16. Crie a class ViewSet:

```
    class CantorViewSet(viewsets.ModelViewSet): #já temos modelo vinculado, por isso usar o ModelViewSet
        queryset = Cantor.objects.all() # indicará o queryset que utilizaremos
        serializer_class = CantorSerializer #classe responsavel por serializar


    class PaisViewSet(viewsets.ModelViewSet):
        """Exibindo todos os países"""
        queryset = Pais.objects.all()
        serializer_class = PaisSerializer
```
    
Informação! queryset busca dados no db

# CONFIGURAR URLS

17. No url.py:

```
    from django.contrib import admin
    from turne.views import CantorViewSet, PaisViewSet
    from rest_framework import routers  será usada como rota default no browser
    from django.urls import path, include
```
    
18. Registrar as rotas do router a serem utilizada:

```
    router = routers.DefaultRouter() # é a rota principal
    router.register('cantor', CantorViewSet, basename='Cantores')
    router.register('pais', PaisViewSet, basename='Paises')
```
    
19. Incluir as rotas na URL:
```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        path('cantor/<int:pk>/', CantorViewSet.as_view()),
        path('paise/<int:pk>/', PaisViewSet.as_view())
    ]
```
