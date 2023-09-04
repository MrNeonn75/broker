from django.urls import path
from . import views

urlpatterns = [
    path('liked/', views.liked, name='liked'),
    path('saved/', views.saved, name='saved'),
    path('delete-saved-post/<int:id>/', views.delete_saved_post, name="delete-saved-post"),
    path('delete-liked-post/<int:id>/', views.delete_liked_post, name="delete-liked-post"),
    path('delete-saved-post/<int:id>/', views.delete_saved_post_detail, name="delete-detail-saved-post"),
    path('delete-liked-post/<int:id>/', views.delete_liked_post_detail, name="delete-detail-liked-post"),
]
