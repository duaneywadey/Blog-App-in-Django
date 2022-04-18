from django import forms
from .models import PostModel, Comment


# We created our forms.py file for creating records

class PostModelForm(forms.ModelForm):

	# Customizing the size of our forms
	content = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
	class Meta:
		# make a form from 'PostModel'
		model = PostModel

		# access these fields
		fields = ('content',)

class PostUpdateForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

	class Meta:
		model = PostModel
		fields = ('content', )


class CommentForm(forms.ModelForm):

	content = forms.CharField(
		label='', widget=forms.TextInput(attrs={
			'placeholder':"What's on your mind?",
			'rows':3

			}))

	class Meta:
		model = Comment
		fields = ('content',)