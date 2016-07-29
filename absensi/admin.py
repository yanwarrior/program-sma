from django.contrib import admin
from .models import Kelas

class KelasAdmin(admin.ModelAdmin):
	list_display = ['id_kelas', 'kelas']


admin.site.register(Kelas, KelasAdmin)

