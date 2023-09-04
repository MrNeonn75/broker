from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.signin  , name='sign-in'),
    path('exit/', views.exit, name='exit'),
    path('log-in/', views.login_funtion, name='log-in'),
    path('log-in/index', views.login_redirect, name='login-index'),
    path('log-in/login-redirect', views.login_redirect, name='login-redirect'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
