from django.urls import reverse
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])