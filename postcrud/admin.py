from django.contrib import admin
from .models import Post, Scrap, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(Scrap)
admin.site.register(Like)