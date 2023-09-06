from django.db import models
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='product_image')
    quantity = models.IntegerField(default=0)
    country = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
# Create your models here.
