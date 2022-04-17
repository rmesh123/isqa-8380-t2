from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
