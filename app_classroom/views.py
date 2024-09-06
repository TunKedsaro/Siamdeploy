from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Student
from django.db.models import Min
from django.db.models.functions import TruncDate
from zcode.yolo_model3 import img_predict,pil_image_to_base64
import matplotlib.pyplot as plt
# data = [
#     {'id':1,'room':1,'date':datetime(2024,8,1),'time':'120000','image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACFSURBVHgBXVBJEsMwCBMe//+xIVxLWUSc9sAwgAQScgEfE4ECMPfKEXJHZniErCw0ANaAJvSwspGwE50N7W0yGyYrwZuNnzN2es5LvsnCHxizbfpLD7ODxqgRynq/NeXgamPlugis9+MumAma83T/1Gs0vEClL4k0dt7Ds/OScnk3cf6JL1E8ilsFjEzgAAAAAElFTkSuQmCC'},
#     {'id':2,'room':2,'date':datetime(2024,8,1),'time':'121000','image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACkSURBVHgBTVDbDkMhCIPF/0/2qweNl4c5WiDbg0G0LS36vOUztootkbEuq23R7jXP7d43Nvs6yMGTIBnbP5coqh8SGtDDWTZd7VCJClWdfMcBcJIt3RvedyjFpAABTEU76WenpyCqhSrfGzxBaYQ3YTB4zt6mMkOrcVDCx7MIYmqroEydKaEEUK0k05el+6p9/YEkAqnkin7rybG1EmEIEDM9wF93oeMQPWy5kgAAAABJRU5ErkJggg=='},
#     {'id':3,'room':1,'date':datetime(2024,8,2),'time':'120000','image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAClSURBVHgBVVFRFsMgDAKfd9j9j7jqPicLifatX6kECEmJ92txChpCi4qoHCLHym+MpTbB/iBd0XSdEkyeS/wg8Y4BNjfiwVDagYEhSLhElWMQEwiSlZvEIjmCQpx4b6FCPO5Mm+RcdnMUx+uZ6Q/YTpnVI7UNIuP3zlRjUsAirxTdWzOX0TnH2bomlLtaEs64sbCF5ZgnKnK3rRVu7uq7HUftH4AfLRrQA32ZT/gAAAAASUVORK5CYII='},
#     {'id':4,'room':2,'date':datetime(2024,8,2),'time':'121000','image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAClSURBVHgBVVFRFsMgDAKfd9j9j7jqPicLifatX6kECEmJ92txChpCi4qoHCLHym+MpTbB/iBd0XSdEkyeS/wg8Y4BNjfiwVDagYEhSLhElWMQEwiSlZvEIjmCQpx4b6FCPO5Mm+RcdnMUx+uZ6Q/YTpnVI7UNIuP3zlRjUsAirxTdWzOX0TnH2bomlLtaEs64sbCF5ZgnKnK3rRVu7uq7HUftH4AfLRrQA32ZT/gAAAAASUVORK5CYII='},
# ]

# # Create your views here.
# def classrooms(request):
#     all_data = Student.objects.order_by('room')
#     context = {'classrooms':all_data}
#     print(context)
#     return render(request,'app_classroom/classrooms.html',context)


def classrooms(request):
    first_images = Student.objects.annotate(
        truncated_date=TruncDate('date')
    ).values('room', 'truncated_date').annotate(
        min_id=Min('id')
    ).values('min_id')
    first_image_records = Student.objects.filter(id__in=first_images)

    context = {'classrooms': first_image_records}
    return render(request, 'app_classroom/classrooms.html', context)

def classroom(request, classroom_id):
    print("->classroom input id:", classroom_id)
    selected_image = Student.objects.get(id=classroom_id)
    print("->selected_image",selected_image)
    
    truncated_date = selected_image.date.date()
    print("->truncated_date",truncated_date)
    
    images = Student.objects.filter(
        room=selected_image.room,
        date__date=truncated_date
    ).order_by('date')
    print("->images",images)

    student_data = []
    for image in images:
        output_img, output_student = img_predict(image.image)
        # plt.imshow(output_img)
        # plt.show()
        student_data.append({
            'image':image,
            'output_image':pil_image_to_base64(output_img),
            'num_student':output_student
        })
    # print(student_data)


#     seated = {'A1': True,
#  'A2': True,
#  'A3': False,
#  'A4': False,
#  'A5': False,
#  'A6': True,
#  'A7': True,
#  'A8': True,
#  'B1': False,
#  'B2': True,
#  'B3': True,
#  'B4': True,
#  'B5': True,
#  'B6': True,
#  'B7': True,
#  'B8': True,
#  'C1': False,
#  'C2': True,
#  'C3': True,
#  'C4': True,
#  'C5': False,
#  'C6': True,
#  'C7': True,
#  'C8': True,
#  'D1': False,
#  'D2': True,
#  'D3': False,
#  'D4': True,
#  'D5': True,
#  'D6': True,
#  'D7': True,
#  'D8': True,
#  'E1': False,
#  'E2': True,
#  'E3': False,
#  'E4': False,
#  'E5': True,
#  'E6': True,
#  'E7': True,
#  'E8': True,
#  'F1': True,
#  'F2': True,
#  'F3': True,
#  'F4': True,
#  'F5': True,
#  'F6': True,
#  'F7': True,
#  'F8': True,
#  'G1': True,
#  'G2': True,
#  'G3': True,
#  'G4': True,
#  'G5': True,
#  'G6': True,
#  'G7': True,
#  'G8': True,
#  'H1': False,
#  'H2': True,
#  'H3': True,
#  'H4': True,
#  'H5': True,
#  'H6': True,
#  'H7': True,
#  'H8': True,
#  'H9': True}
    
    context = {'student_data': student_data, 
               'selected_image': selected_image,
               'seat':{'A1':True}
    }
    return render(request, 'app_classroom/classroom.html', context)




