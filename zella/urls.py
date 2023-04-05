from django.urls import path
from . import views

app_name = 'zella'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('quizes/', views.quizes, name='quizes'),
    path('startquiz/<int:quiz_id>/', views.startquiz, name='startquiz'),
    path('profile/', views.profile, name='profile'),
    path('units/', views.units, name='units'),
    path('courses/', views.courses, name='courses')
]