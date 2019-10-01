from django.db import models
from django.urls import reverse

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=200) 

    def __str__(self): return self.title
   
class Post(models.Model):
    title = models.CharField(max_length=200) 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    
    def __str__(self): 
        return self.title

    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.pk)])