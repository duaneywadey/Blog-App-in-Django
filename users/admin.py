from django.contrib import admin
from .models import ProfileModel, Message

class MessageModelAdmin(admin.ModelAdmin):
	list_display = ('user', 'content', 'created_at')

admin.site.register(ProfileModel)
admin.site.register(Message, MessageModelAdmin)
