from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')


    return render(request, 'login.html')
def logout(request):
    print("hi")
    auth.logout(request)
    return redirect('/credit/index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username):
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.success(request, 'Registered successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')
