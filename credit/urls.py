from . import views
from django.urls import path,include

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout')

]