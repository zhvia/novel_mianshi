from django.conf.urls import url
from textApp import views

urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r'img/', views.img, name='image'),
    url(r'login/', views.login, name='login'),
    url(r'logout/', views.logout, name='logout'),
    url(r'search/', views.search, name='search'),
    url(r'my_zone/', views.my_zone, name='my_zone'),
    url(r'add_book/', views.add_book, name='add_book'),
    url(r'chapter/', views.chapter, name='chapter'),
    url(r'chapter_info/', views.chapter_info, name='chapter_info'),
    url(r'register/', views.register, name='register'),
    url(r'vip/', views.vip, name='vip'),
    url(r'chapter_normal/', views.chapter_normal, name='chapter_normal'),
    url(r'is_on_book/', views.is_on_book, name='is_on_book'),
    url(r'my_books/', views.my_books, name='my_books'),
    url(r'delete_mybook/', views.delete_mybook, name='delete_mybook'),
    # url(r'python_bug/', views.python_bug, name='python_bug')
]

