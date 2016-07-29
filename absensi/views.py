from django.shortcuts import render
from .models import Kelas


def kelas_index(request):
	semua_kelas = Kelas.objects.all()
	return render(request, 'absensi/kelas/index.html', {'semua_kelas': semua_kelas})
