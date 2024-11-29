from django.contrib import admin
from .models import CustomUser, Setor, TipoEquipamento, Equipamento

admin.site.register(CustomUser)
admin.site.register(Setor)
admin.site.register(TipoEquipamento)
admin.site.register(Equipamento)
