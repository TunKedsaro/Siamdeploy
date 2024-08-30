from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def classrooms(request):
    return render(request,'app_classroom/classrooms.html')

def classroom(request,classroom_id):
    print("classroom input id:",classroom_id)
    context = {'num':classroom_id}
    return render(request, 'app_classroom/classroom.html',context)