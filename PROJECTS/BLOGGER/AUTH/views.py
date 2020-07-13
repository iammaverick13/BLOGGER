from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import *
# Create your views here.
def userExist(request):
	context = {
		'pageTitle':'DAFTAR',
	}
	return render(request, 'user/user_exist.html', context)

def registerView(request):
	user = None
	check_password = False
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		a = User.objects.all()
		
		for i in a:
			if username == i.username or email == i.email:
				return userExist(request)

		if password1 != password2:
			check_password = True

		else:
			user = User.objects.create_user(username=username, email=email, password=password1)
			profile = Profile.objects.create(user=user, gender='', age=0)
			profile.save()
			
			login(request, user)
			return redirect('/'+str(user.id))

	context = {
		'pageTitle':'DAFTAR',
		'check_password':check_password,
		'user':user
	}

	return render(request, 'user/register.html', context)

def loginView(request):
	condition = False
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('/'+str(user.id))
		else:
			condition = True
	context = {
		'condition':condition,
	}

	return render(request, 'user/login.html', context)

def logoutView(request):
	logout(request)
	return redirect('/')

from BLOG.models import *

def dashboardView(request, id, filter='all'):
	form = ImgForm()
	user = User.objects.get(id=id)
	profile = Profile.objects.get(user__id=id)
	
	if filter == 'all':
		blogs = Blog.objects.filter(user__id=id)
	else:
		blogs = Blog.objects.filter(title__icontains=filter)

	if request.method == 'POST':
		form = ImgForm(request.POST, request.FILES)
		if form.is_valid():
			profile.img = form.cleaned_data.get('img')
			profile.save()
			return redirect('/accounts/dashboard/'+str(user.id))
	else:
		form = ImgForm()

	context = {
		'form':form,
		'blogs':blogs,
		'profile':profile,
	}
	return render(request, 'user/dashboard.html', context)

from .forms import *

def dashboardUpdateView(request, id):
	user = User.objects.get(id=id)
	profile = Profile.objects.get(user__id=id)
	form = UpdateDashboardForm(instance=profile)

	if request.method == 'POST':
		form = UpdateDashboardForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('/accounts/dashboard/'+str(user.id))
	else:
		form = UpdateDashboardForm()

	context = {
		'form':form,
	}

	return render(request, 'user/update_dashboard.html', context)