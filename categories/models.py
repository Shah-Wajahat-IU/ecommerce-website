
from tabnanny import verbose
from django.db import models
from django.forms import CharField

# Create your models here.
class Categories(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    cat_img=models.ImageField(upload_to='photos/categories', height_field=None, width_field=None, blank=True)

    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"

    def __str__(self):
        return self.category_name

    def __unicode__(self):
        return 