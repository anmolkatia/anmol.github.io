from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['repeat-pass']
        try:
            Terms = request.POST['remember-me']
        except:
            Terms= ""

        if (password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
                print("Username Taken")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('register')
                print("Email Already Exist")

            elif Terms != "terms agreed":
                messages.info(request, "Need to agree Terms First")
                return redirect('register')
                print("Need to agree Terms First")

            else:

                user = User.objects.create_user(password=password1, username=username, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.info(request, "Registration Successful")
                return redirect('register')
                print('user created')

        else:
            messages.info(request, "Password Doesnt Match ")
            return redirect('register')
            print("password not matching")

    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password Doesnt Match')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
