from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def home(request):
    return render(request,'app_general/home.html')

def about(request):
    return render(request,'app_general/about.html')

def realtime(request):
    return render(request,'app_general/realtime.html')

def upload_image(request):
    return render(request,'app_general/upload_image.html')

def video_extract(request):
    return render(request,'app_general/video_extract.html')
