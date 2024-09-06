from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def home(request):
    return render(request,'app_general/home.html')

def about(request):
    context = {'A1': True,
 'A2': True,
 'A3': False,
 'A4': False,
 'A5': False,
 'A6': True,
 'A7': True,
 'A8': True,
 'B1': False,
 'B2': True,
 'B3': True,
 'B4': True,
 'B5': True,
 'B6': True,
 'B7': True,
 'B8': True,
 'C1': False,
 'C2': True,
 'C3': True,
 'C4': True,
 'C5': False,
 'C6': True,
 'C7': True,
 'C8': True,
 'D1': False,
 'D2': True,
 'D3': False,
 'D4': True,
 'D5': True,
 'D6': True,
 'D7': True,
 'D8': True,
 'E1': False,
 'E2': True,
 'E3': False,
 'E4': False,
 'E5': True,
 'E6': True,
 'E7': True,
 'E8': True,
 'F1': True,
 'F2': True,
 'F3': True,
 'F4': True,
 'F5': True,
 'F6': True,
 'F7': True,
 'F8': True,
 'G1': True,
 'G2': True,
 'G3': True,
 'G4': True,
 'G5': True,
 'G6': True,
 'G7': True,
 'G8': True,
 'H1': False,
 'H2': True,
 'H3': True,
 'H4': True,
 'H5': True,
 'H6': True,
 'H7': True,
 'H8': True,
 'H9': True}
    data = {"seat":context}
    return render(request,'app_general/about.html',data)

def realtime(request):
    return render(request,'app_general/realtime.html')

def upload_image(request):
    return render(request,'app_general/upload_image.html')

def video_extract(request):
    return render(request,'app_general/video_extract.html')
