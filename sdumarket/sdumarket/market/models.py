from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.TextField(blank=True)
	quantity = models.IntegerField()
	category_id = models.ForeignKey('Category', on_delete=models.CASCADE)