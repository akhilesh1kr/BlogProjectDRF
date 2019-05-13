from django.contrib import admin
from .models import Post

# admin.site.register(Post)

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'publish']
