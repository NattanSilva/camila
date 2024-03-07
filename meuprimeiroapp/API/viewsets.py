from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import Cadastro
from .serializers import CadastroSerializer
import requests

class CadastroViewSet(ModelViewSet):
  queryset = Cadastro.objects.all()
  serializer_class = CadastroSerializer

  def create(self, request):
    nome = request.data.get('nome')
    ultimo_nome = request.data.get('ultimo_nome')
    numero = request.data.get('numero')
    genero = request.data.get('genero')