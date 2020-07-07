from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html')

def userHome(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user_home.html')