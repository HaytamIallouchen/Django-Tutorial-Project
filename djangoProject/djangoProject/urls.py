"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Tutorial import views
app_name = 'Tutorial'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('authors/add/', views.addauthor, name="authoradd"),
    path('authors/delete/<int:pk>/', views.deleteauthor, name='authordelete'),
    path('books/', views.BookListView.as_view(), name="books"),
    path('books/add/', views.addbook, name="bookadd"),
    path('books/delete/<int:pk>/', views.deletebook, name='bookdelete'),
    path('books/<int:pk>/', views.booksbyauthor, name="belongstoauthor")
]
