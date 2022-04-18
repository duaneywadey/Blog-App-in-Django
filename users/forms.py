from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel, Message

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


# -----------------DELETING HELP TEXT---------------
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None


# Form for updating username and email
class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'email']:
			self.fields[fieldname].help_text = None



# Form for updating photos
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = ['avatar']

class MessageForm(forms.ModelForm):

	content = forms.CharField(
		label='', widget=forms.TextInput(attrs={
			'placeholder':"What's on your mind?",
		




			}))

	class Meta:
		model = Message
		fields = ('content', )








