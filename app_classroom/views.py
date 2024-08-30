from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def classrooms(request):
    return render(request,'app_classroom/classrooms.html')