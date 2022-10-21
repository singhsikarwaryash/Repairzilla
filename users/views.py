from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
#from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']

#     user  = authenticate(request, username=username, password=password)
#     if user  is not None:
#         login(request, 'users/service.html')
#     else:
#         login(request, 'users/login.html')

@login_required()
def profile(request):
    return render(request, 'users/profile.html')

def service(request):
    return render(request, 'users/service.html')

def contact(request):
    return render(request, 'users/contact.html')

