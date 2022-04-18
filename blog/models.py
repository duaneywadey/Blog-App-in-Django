from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class PostModel(models.Model):
	content = models.TextField()

	# We added 'on_delete=models.CASCADE' so that whenever an author is deleted,
	# all his posts as well will be deleted
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)


	# To sort our posts according to date, we need to put comma to make it a tuple or list
	class Meta:
		ordering = ('-date_created', )


	# Get the number of comments
	def commentCount(self):
		return self.comment_set.all().count()

	def comments(self):
		return self.comment_set.all()






		

	# Defines how our model will appear on django's admin panel
	def __str__(self):
		return f'{self.author}'


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)


	def __str__(self):
		return self.content

	

