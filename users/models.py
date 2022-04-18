from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class ProfileModel(models.Model):
	# One user from django admin is equal to one profile (One to one)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='profile', default='avatar.jpg', validators=[
		FileExtensionValidator(['png', 'jpg'])])

	def __str__(self):
		return f'{self.user.username}'


class Message(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'{self.content}'

