from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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

def dashboardView(request, id):
	user = User.objects.get(id=id)
	return render(request, 'user/dashboard.html')		