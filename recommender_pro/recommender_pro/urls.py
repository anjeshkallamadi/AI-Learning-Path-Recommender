
from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/generate/', views.generate_path),
    path('' , views.prototype_home),
    
]
