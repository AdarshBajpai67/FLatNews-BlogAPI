from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title','status', 'author',)
    list_filter =  ('published_date',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)