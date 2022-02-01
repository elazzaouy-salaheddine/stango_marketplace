from django.db import models
from product.models import Product


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User',
                              related_name='comments',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='comments',
                                on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
