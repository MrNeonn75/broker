from django.db import models
from accounts.models import Accounts
from property.models import ProductModel

class LikeModel(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    post = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.user.email} Post: {self.post.product_name}'
    
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

class SaveModel(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    post = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.user.email} Post: {self.post.product_name}'
    
    class Meta:
        verbose_name = 'Saved post'
        verbose_name_plural = 'Saved posts'