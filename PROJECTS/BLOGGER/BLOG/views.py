from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import *
from AUTH.models import *
from .models import *
# Create your views here.
def addBlog(request, id):
    user = User.objects.get(id=id)
    form = AddBlogForm()
    
    if request.method == 'POST':
        form = AddBlogForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            body=form.cleaned_data.get('body')
            user_blog = Blog.objects.create(user=user, title=title, body=body)
            user_blog.save()
            return redirect('/accounts/dashboard/'+str(user.id))
    else:
        form = AddBlogForm()

    context = {
        'form':form,
    }

    return render(request, 'blog/add_blog.html', context)

def deleteBlog(request, id, title):
    blog = Blog.objects.get(title=title)
    user = User.objects.get(id=id)
    blog.delete()
    return redirect('/accounts/dashboard/'+str(user.id))

def updateBlog(request, id, slug):
    blog = Blog.objects.get(slug=slug)
    user = User.objects.get(id=id)
    form = AddBlogForm(instance=blog)

    if request.method == 'POST':
        form = AddBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/accounts/dashboard/'+str(user.id))
    else:
        form = AddBlogForm()

    context = {
        'form':form,
    }

    return render(request, 'blog/add_blog.html', context)
