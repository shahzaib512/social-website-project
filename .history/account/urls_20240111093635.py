from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # change password urls
    path('password-change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    
    # reset password urls
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password-reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    
    path('', views.dashboard, name='dashboard'),
]