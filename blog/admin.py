from django.contrib import admin
from .models import Proyecto
from .models import Carrera
from .models import Empresa


admin.site.register(Proyecto)
admin.site.register(Carrera)
admin.site.register(Empresa)
