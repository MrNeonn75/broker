from django.db import models
from datetime import datetime

class BlogModel(models.Model):
    post_title = models.CharField('Ad', max_length=200)
    post_subtitle = models.TextField('Altyazı')
    post_article = models.TextField('Məzmun')
    post_date = models.DateTimeField('Tarix', default=datetime.now())
    post_image_link = models.CharField('Link', max_length=250, null=True, blank=True)
    post_image1 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/')
    post_image2 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/')
    post_image3 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image4 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image5 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image6 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image7 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image8 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image9 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    post_image10 =  models.ImageField('Image', upload_to='BlogPosts/%Y/%m/%d/', blank=True, null=True)
    

    def __str__(self):
        return self.post_title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
