from django.contrib import admin
from .models import Cliente, TipoPropiedad, Propiedad, Contrato, ContratoEstado
# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoPropiedad)
admin.site.register(Propiedad)
admin.site.register(Contrato)
admin.site.register(ContratoEstado)
