from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    #return HttpResponse("signup")
    if request.method == 'POST':
        # User has info and wants account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error':'Passwords do not match'})
    else:
        return render(request,'signup.html')

def login(request):
    #return HttpResponse("login")
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    #TODO Need to route to homepage
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')