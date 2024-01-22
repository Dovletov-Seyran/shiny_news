from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return f"{self.id}. {self.name}"


class News(models.Model):
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='media/', null=True)
    image2 = models.ImageField(upload_to='media/', null=True, blank=True)
    image3 = models.ImageField(upload_to='media/', null=True, blank=True)
    image4 = models.ImageField(upload_to='media/', null=True, blank=True)
    image5 = models.ImageField(upload_to='media/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.name
