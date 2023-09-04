from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Accounts
from datetime import datetime

def validate_single_word(value):
    words = value.split()
    if len(words) > 1:
        raise ValidationError("Yanlız bir söz yazmağa icazə var.")

class CategoryModel(models.Model):
    category = models.CharField("Category name", max_length=100, validators=[validate_single_word])

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class AreaModel(models.Model):
    area = models.CharField('Area', max_length=200)
    
    def __str__(self):
        return self.area
    
    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'

class ProductModel(models.Model):
    product_name = models.CharField('Product name', max_length=100)
    product_price = models.FloatField('Product price')
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_article = models.TextField('Product article')
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    date = models.DateTimeField('Date', default=datetime.now())
    square = models.FloatField('Square', default=15.0)
    rooms = models.IntegerField('Rooms', default=1)
    image1 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/')
    image2 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/')
    image3 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image4 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image5 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image6 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image7 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image8 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image9 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    image10 =  models.ImageField('Image', upload_to='posts/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

class CommentModel(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    post = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    comment = models.TextField('Comment')
    comment_date = models.DateTimeField('Date', default=datetime.now())

    def __str__(self):
        return f'{self.user.email} -> {self.post.product_name}'
    
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

class CommentReplyModel(models.Model):
    user_reply = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    main_comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    post = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    reply = models.TextField('Reply')
    reply_date = models.DateTimeField('Reply date', default=datetime.now())

    def __str__(self):
        return f'{self.user_reply.email} -> {self.main_comment.user.email}'
    
    class Meta:
        verbose_name = 'reply'
        verbose_name_plural = 'replies'