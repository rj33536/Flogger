from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
	commentator = models.ForeignKey(User,on_delete = models.CASCADE, related_name="commmentator")
	text = models.TextField()

class blog(models.Model):
	author = models.ForeignKey(User,on_delete = models.CASCADE, related_name="author")
	title = models.CharField(max_length = 300)
	text = models.TextField()
	created_date = models.DateTimeField(blank=True,null=True)
	publish_date = models.DateTimeField(blank = True,null = True)
	claps = models.ManyToManyField(User, related_name="clappers")
	comments = models.ManyToManyField(Comment, related_name="comments")
	def publish(self):
		self.publish_date = timezone.now()
		self.created_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title + " " + self.text

