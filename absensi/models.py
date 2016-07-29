from django.db import models

class Kelas(models.Model):
	id_kelas = models.CharField(max_length=2, unique=True)
	kelas = models.CharField(max_length=32)

	def __str__(self):
		return self.id_kelas

	class Meta:
		db_table = 'kelas'
		ordering = ('id_kelas',)
