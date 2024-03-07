from rest_framework.serializers import ModelSerializer
from ..models import Cadastro

class CadastroSerializer(ModelSerializer):
  class Meta:
    model = Cadastro
    fields = ['nome', 'ultimo_nome', 'telefone', 'genero']