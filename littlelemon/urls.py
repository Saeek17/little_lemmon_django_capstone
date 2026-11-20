from django.contrib import admin
from django.urls import path, include
from restaurant.views import home
urlpatterns = [path('', home, name='home'), path('admin/', admin.site.urls), path('api/', include('restaurant.urls')), path('auth/', include('djoser.urls')), path('auth/', include('djoser.urls.authtoken')), path('api/token/', include('rest_framework_simplejwt.urls'))]
