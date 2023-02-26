from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.info, name='info'),
    path('about/', views.about, name='about'),
]