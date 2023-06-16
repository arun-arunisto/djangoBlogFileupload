from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    blog_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title