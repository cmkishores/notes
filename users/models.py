from django.db import models
from django.contrib.auth.admin import AbstractUser

class CustomUser(AbstractUser):
	GENDER_CHOICES = [ 
	
	('M','Male'),
	('F','Female'),

	]
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES) 

# Create your models here.
