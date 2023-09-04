from django.db import models
from property.models import ProductModel
from datetime import datetime


class CampaignModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    campaign_price = models.FloatField('Price')
    start_date = models.DateTimeField('Start date', default=datetime.now())
    final_date = models.DateTimeField('Final date')

    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'
