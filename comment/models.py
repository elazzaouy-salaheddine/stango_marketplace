from django.db import models
from product.models import Product


class Comment(models.Model):
    custemer_name = models.CharField(max_length=255)
    custemer_email = models.EmailField()
    body = models.TextField(blank=False)
    review = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    add_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['add_at']
