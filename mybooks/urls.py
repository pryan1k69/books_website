from django.urls import path
from . import views



urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/update', views.BooksUpdateView.as_view(), name='books_update'),
    path('profile/<int:pk>/delete', views.BooksDeleteView.as_view(), name='books_delete'),
    path('profile/create', views.create, name='create'),
]