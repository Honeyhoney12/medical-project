from django.urls import path
from .views import disease_list, disease_detail, login_view
from . import views
urlpatterns = [
      path('logout/', views.logout_view, name='logout'),
     path('register/', views.register_view, name='register'), 
    path('', disease_list, name='disease_list'),
    path('disease/<int:pk>/', disease_detail, name='disease_detail'),
    path('login/', login_view, name='login'),
]
from django.conf import settings
from django.conf.urls.static import static

