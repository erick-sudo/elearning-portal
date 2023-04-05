from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

from .models import ZellaUser

from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'zella/index.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/zella/login')

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('/zella/')
        return render(request, "zella/login.html")
    elif request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            #return render(request, "zella/index.html")
            return HttpResponseRedirect('/zella/')
        else:
            # Show an error message
            return render(request, "zella/login.html", {'error': 'Invalid username or password', 'username': username, 'password': password})

def register(request):
    if request.method == 'GET':
        return render(request, "zella/register.html")
    else:
        username = request.POST.get('username', '')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if(password != confirm_password):
            print("Passwords did not match")
            return render(request, 'zella/register.html', {
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'password': password,
                'confirm_password': confirm_password
            })

        try:
            ZellaUser.objects.create(username=username, firstname=firstname, lastname=lastname, email=email, password=password)
        except ValidationError:
            print("Validation Errors")
            return render(request, 'zella/register.html', {
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'password': password,
                'confirm_password': confirm_password
            })
        except:
            return render(request, 'zella/register.html', {
                'integrity': "Username already taken",
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'password': password,
                'confirm_password': confirm_password
            })

        return HttpResponseRedirect('/zella/login')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/zella/login')

def quizes(request):
    return render(request, 'zella/quizes.html')

def profile(request):
    return render(request, 'zella/profile.html')