from django.urls import path
from app_general import views

urlpatterns = [
    path('',views.home,name='home')
]
