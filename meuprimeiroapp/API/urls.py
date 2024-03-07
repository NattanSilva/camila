from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import CadastroViewSet

router = DefaultRouter()
router.register('cadastro', CadastroViewSet)

urlpatterns = [
  path('api/',include(router.urls))
]