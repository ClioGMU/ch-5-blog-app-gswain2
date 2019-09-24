from django.db import models

class Catagory(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=200) 

    def __str__(self): return self.title
   
class Post(models.Model):
    title = models.CharField(max_length=200) 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    
    def __str__(self): return self.title