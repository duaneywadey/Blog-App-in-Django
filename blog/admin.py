from django.contrib import admin
from .models import PostModel, Comment


# Register your models here.

# We added this class to create a table on django admin for visualization
class PostModelAdmin(admin.ModelAdmin):
	list_display = ('author', 'date_created')

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)
