from django.urls import path
from . import views

app_name = 'zella'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signupform'),
    path('quizes/', views.quizes, name='quizes'),
    path('profile/', views.profile, name='profile'),
]