
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('search.urls')),
    path('admin/', admin.site.urls),
]
