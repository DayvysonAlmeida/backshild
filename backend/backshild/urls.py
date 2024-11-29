from rest_framework.routers import DefaultRouter
from .views import EquipamentoViewSet, SetorViewSet, TipoEquipamentoViewSet

router = DefaultRouter()
router.register('setores', SetorViewSet)
router.register('tipos-equipamento', TipoEquipamentoViewSet)
router.register('equipamentos', EquipamentoViewSet)

urlpatterns = router.urls
