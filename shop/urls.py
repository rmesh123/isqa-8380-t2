from django.urls import re_path as url
from . import views
from django.urls import path
from .views import PackageDetailView, PackageListView

app_name = 'shop'
urlpatterns = [
    path('<int:pk>', PackageDetailView.as_view(), name='product'),
    path('', PackageListView.as_view(), name='homepage'),
]
