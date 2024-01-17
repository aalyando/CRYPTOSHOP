from django.contrib import admin
from django.urls import path, include
from djangoStore import views

urlpatterns = [
    path("", views.base, name='admin'),
    path('admin/', admin.site.urls),
    path('user/', include('user_info.urls')),
    path('product/', include('products.urls')),
]
