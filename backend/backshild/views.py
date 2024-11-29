from rest_framework.viewsets import ModelViewSet
from .models import Equipamento, Setor, TipoEquipamento
from .serializers import EquipamentoSerializer, SetorSerializer, TipoEquipamentoSerializer

class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class TipoEquipamentoViewSet(ModelViewSet):
    queryset = TipoEquipamento.objects.all()
    serializer_class = TipoEquipamentoSerializer

class EquipamentoViewSet(ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
