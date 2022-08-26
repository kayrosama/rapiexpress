from django.contrib import admin
from .models import Usuarios, TipoDocumento, UsuarioDocumento, AeroLinea, UsuarioVuelo, Direccion, Empresa, Agencia, Rastreo, PaqueteEncabezado, PaqueteDetalle

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(TipoDocumento)
admin.site.register(UsuarioDocumento)
admin.site.register(AeroLinea)
admin.site.register(UsuarioVuelo)
admin.site.register(Direccion)
admin.site.register(Empresa)
admin.site.register(Agencia)
admin.site.register(Rastreo)
admin.site.register(PaqueteEncabezado)
admin.site.register(PaqueteDetalle)
