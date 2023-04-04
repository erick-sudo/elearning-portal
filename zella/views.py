from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'zella/login.html')

def signup(request):
    return render(request, 'zella/register.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render(request, "zella/index.html")
    else:
        # Show an error page
        return HttpResponseRedirect("zella/error.html")

def register(request):
    return render(request, 'zella/register.html')

def quizes(request):
    return render(request, 'zella/quizes.html')

def profile(request):
    return render(request, 'zella/profile.html')