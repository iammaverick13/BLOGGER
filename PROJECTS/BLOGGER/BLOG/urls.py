from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [
    path('add/<int:id>/', addBlog, name='add_blog'),
    path('delete/<int:id>/<str:title>/', deleteBlog, name='delete_blog'),
    path('update/<int:id>/<str:slug>/', updateBlog, name='update_blog'),
]