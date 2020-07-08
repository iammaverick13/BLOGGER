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