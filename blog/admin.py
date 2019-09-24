from django.contrib import admin 
from .models import Post, Catagory

class CatagoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Catagory, CatagoryAdmin)

admin.site.register(Post)