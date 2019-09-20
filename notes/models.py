from django.db import models
from django.urls import reverse

class Note(models.Model):
	title = models.CharField(max_length=30)
	detail = models.TextField()

	def __str__(self):
		return self.title[:30]
	
	def get_absolute_url(self):
		return reverse('detailed', args=[str(self.id)])

# Create your models here.
