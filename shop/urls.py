from .views import *
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'shop'
urlpatterns = [
    path('<int:pk>', PackageDetailView.as_view(), name='product'),
    path('', PackageListView.as_view(), name='homepage'),
    path('signup', signup, name='signup'),

    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/forgot_password.html"),
         name='forgot_password'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
         name='password_reset_complete'),

    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="registration/changedpassword.html"),
         name='changedpassword'),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(template_name="registration/changePassword.html"),
         name='changePassword'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_item, name="update_item"),
    path('process_order/', views.process_order, name="process_order"),
]
