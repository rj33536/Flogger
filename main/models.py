from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class blog(models.Model):
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	title = models.CharField(max_length = 300)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now())
	publish_date = models.DateTimeField(blank = True,null = True)
	
	def publish(self):
		self.publish_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title	
