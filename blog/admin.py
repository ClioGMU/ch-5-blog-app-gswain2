from django.contrib import admin 
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

admin.site.register(Post)