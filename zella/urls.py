from django.urls import path
from . import views

app_name = 'zella'
urlpatterns = [
    path('home/', views.index, name='index'),
]