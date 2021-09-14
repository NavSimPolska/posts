from django.contrib import admin
from post.models import Posts, Author

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'author_id']
    list_filter = ['author_id']
    search_fields = ['title']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick']

# Register your models here.
admin.site.register(Posts, PostAdmin)
admin.site.register(Author, AuthorAdmin)
