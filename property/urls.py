from django.urls import path
from . import views

urlpatterns = [
    path('', views.property, name='property'),
    path('<int:id>/', views.property_detail_view, name='property-detail-view'),
    # path('<str:filter_category>/', views.filter_page, name='category-filter'),
    path('<int:id>/delete-comment/<int:com_id>/', views.remove_comment, name="remove-comment"),
    path('like/<int:id>/', views.like_post, name='like-post'),
    path('save/<int:id>/', views.save_post, name='save-post'),
    # path('<int:filter>/', views.property_filter, name='property-filter'),
]
