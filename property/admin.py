from django.contrib import admin
from .models import ProductModel, CategoryModel, AreaModel, CommentModel, CommentReplyModel

admin.site.register(CategoryModel)
admin.site.register(AreaModel)
admin.site.register(ProductModel)
admin.site.register(CommentModel)
admin.site.register(CommentReplyModel)
