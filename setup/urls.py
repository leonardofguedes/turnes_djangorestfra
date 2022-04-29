from django.contrib import admin
from django.urls import path, include
from turne.views import CantorViewSet, PaisViewSet, TurneViewSet, ListaTurnesCantorViewSet, TurnesPaisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cantor', CantorViewSet, basename='Cantores')
router.register('pais', PaisViewSet, basename='Paises')
router.register('turne', TurneViewSet, basename='Turnes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cantor/<int:pk>/turne/', ListaTurnesCantorViewSet.as_view()),
    path('pais/<int:pk>/turne/', TurnesPaisViewSet.as_view()),

]
