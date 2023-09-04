from django.db.models import EmailField, CharField, TextField
from django.db import models

class ContactModel(models.Model):
    name = CharField('Name', max_length=50)
    user_email = EmailField('Email', max_length=150)
    subject = CharField('Subject', max_length=200)
    message = TextField('Message')

    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'