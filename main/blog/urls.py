from django.urls import path

from blog import views

urlpatterns = [
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
]