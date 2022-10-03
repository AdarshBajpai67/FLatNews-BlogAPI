from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title','status', 'author',)
    list_filter =  ('created_at',)

admin.site.register(Post, PostAdmin)