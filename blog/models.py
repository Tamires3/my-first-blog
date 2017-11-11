from django.db import models
from django.utils import timezone


#class - definindo um objeto \ Post é o nome do nosso modelo
#Nome de classe com letra maiúscula.
class Post(models.Model):
	author = models.ForeignKey("auth.User")#Link para outro modelo
	title = models.CharField(max_length=200) #Texto limitado
	text = models.TextField() #texto longo, sem limite.
	created_date = models.DateTimeField(#Data e hora
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)


	def publish(self): #uma função/método
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title




