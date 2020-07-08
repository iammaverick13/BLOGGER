from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [
    path('add/<int:id>/', addBlog, name='add_blog'),
]