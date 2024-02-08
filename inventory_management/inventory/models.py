from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
	name = models.CharField(max_length=200, verbose_name="Nombre")
	quantity = models.IntegerField(verbose_name="Cantidad")
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoría")
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200, verbose_name="Nombre")

	class Meta:
		verbose_name_plural = 'categorias'

	def __str__(self):
		return self.name