from . import views
from django.urls import path, include

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.UserFormView.as_view(), name='register'),
]