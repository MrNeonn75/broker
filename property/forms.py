from django.forms import CharField, TextInput, Select, FloatField, NumberInput, IntegerField
from django import forms
from .models import CategoryModel, AreaModel, CommentModel, CommentReplyModel

class FilterForm(forms.Form):
    CHOICES_CATEGORY_LIST = ['Kateqoriya']
    CHOICES_AREA_LIST = ['Ərazi']

    for x in list(CategoryModel.objects.all().values()): CHOICES_CATEGORY_LIST.append(x['category'])
    for x in list(AreaModel.objects.all().values()):CHOICES_AREA_LIST.append(x['area'])
    
    CHOICES_CATEGORY = []
    for i in CHOICES_CATEGORY_LIST:
        CHOICES_CATEGORY.append((f'{i}',f'{i}'))

    CHOICES_AREA = []
    for i in CHOICES_AREA_LIST:
        CHOICES_AREA.append((f'{i}',f'{i}'))

    
    search_category = CharField(label='Kateqoriya', required=False, widget=Select(choices=CHOICES_CATEGORY, attrs={
        'placeholder' : 'Kateqoriya',
        'class'       : 'form-control',
        'name'        : 'category'
    }))
    search_area = CharField(label='Ərazi', required=False, widget=Select(choices=CHOICES_AREA, attrs={
        'placeholder' : 'Ərazi',
        'class'       : 'form-control',
        'name'        : 'area'
    }))
    search_rooms = CharField(label = 'Rooms', required=False, widget=NumberInput(attrs={
        'placeholder' : 'Otaq',
        'class'       : 'form-control',
        'name'        : 'rooms'
    }))
    search_min_price = FloatField(label='Min price', required=False, widget=NumberInput(attrs={
        'placeholder' : 'Min büdcə',
        'class' : 'form-control',
        'name'  : 'search_min_price'
    }))
    search_max_price = FloatField(label='Max price', required=False, widget=NumberInput(attrs={
        'placeholder' : 'Max büdcə',
        'class' : 'form-control',
        'name'  : 'search_max_price'
    }))

class SearchForm(forms.Form):
    search = CharField(label='Search', required=False, widget=TextInput(attrs={
        'placeholder' : 'Axtar...',
        'class'       : 'form-control me-2 search-input',
        'name'        : 'search',
    }))

class CommentForm(forms.Form):
    comment = CharField(label='Comment', widget=TextInput(attrs={
        'placeholder' : 'Şərh yazın',
        'class'       : 'form-control',
        'name'        : 'comment',
        'cols'        : '30',
        'rows'        : '1',
        'id'          : 'comment',
    }))

    class Meta:
        model = CommentModel
        fields = ('comment')

class CommentReplyForm(forms.Form): # name="comment-answer" id="comment-answer" cols="30" rows="1" class="form-control"
    comment_reply = CharField(label='Reply', widget=TextInput(attrs={
        'placeholder' : 'Cavabla',
        'class'       : 'form-control ',
        'name'        : 'reply',
        'cols'        : '30',
        'rows'        : '1',
        'id'          : 'comment-answer',
    }))
    # type="hidden" id="hidden_comment_data" name="hidden_comment_data" value="{{ com.id }}"
    comment_hidden_data = IntegerField(label='Hidden data', widget=NumberInput(attrs={
        'type'  : 'number',
        'name'  : 'hidden_comment_data',
        'value' : '1',
        'id'    : 'hidden_comment_data',
        'style' : 'display: none;',
    }))

    class Meta:
        model = CommentReplyModel
        fields = ('reply')