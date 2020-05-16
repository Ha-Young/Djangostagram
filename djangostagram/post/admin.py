from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'description', 'writer', 'img_url', 'registered_dttm')

admin.site.register(Post, PostAdmin)