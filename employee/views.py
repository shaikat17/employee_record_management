from django.shortcuts import render
from .models import *
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
        pwd = request.POST['pwd']

        try:
            User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(empcode=ec)

            error = 'No'
        except:
            error = 'Yes'
    return render(request, 'registration.html')

def emp_login(request):
    return render('emp_login', emp_login, name='emp_login.html')
