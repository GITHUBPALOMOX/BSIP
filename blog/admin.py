from django.contrib import admin
from .models import Proyecto
from .models import Carrera
from .models import Empresa
#from .models import post
#from MYBSIP.blog.models import Proyecto

admin.site.register(Proyecto)
admin.site.register(Carrera)
admin.site.register(Empresa)
#admin.site.register(post)