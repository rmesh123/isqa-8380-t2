from django.urls import re_path as url
from . import views
from django.urls import path

app_name = 'shop'
urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('product', views.product, name='product'),

]
