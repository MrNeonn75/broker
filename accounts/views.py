from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Accounts

class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return 'login-redirect'

def login_funtion(request):
    error = ''
    if(request.method == "POST"):
        form = LoginForm()
    
        if(form.is_valid):
            username_data = request.POST['username']
            password_data = request.POST['password']
            user = authenticate(request, username=username_data, password=password_data)

            if(user is not None):
                if(user.is_active):
                    login(request, user)
                    return redirect('index')
                else:
                    error = 'Disabled account'
            else:
                error = 'Invalid login'
    else:
        form = LoginForm()
    
    data = {
        'form' : form,
    }

    return render(request, 'login.html', data)


def signin(request):
    register_form = RegisterForm()
    if(request.method == 'POST'):
        if(register_form.is_valid):
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']

            if(password1 == password2):
                new_user = Accounts.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                )

                login(request, new_user)

                messages.success(request, 'Account created successfully')
                
                return redirect('index')
            else: messages.error(request, 'First password and second password is not equal!')

    data = {
        'form' : register_form 
    }

    return render(request, 'register.html', data)

def exit(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect('index')
    
def login_redirect(request):
    return redirect('index')

