from django.shortcuts import render
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ''

    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        ec = request.POST['emid']
        pwd = request.POST['psw']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user=user, empcode=ec)

            error = 'No'
        except:
            error = 'Yes'
    return render(request, 'registration.html', locals())

def emp_login(request):
    error = ''
    if request.method == 'POST':
        uName = request.POST['email']
        uPass = request.POST['psw']

        user = authenticate(username=uName, password=uPass)

        if user:
            login(request, user)
            error = 'No'
        else:
            error = 'Yes'
    return render(request, 'emp_login.html', locals())

def emp_home(request):
    return render(request, 'emp_home.html')
