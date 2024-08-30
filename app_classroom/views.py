from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def classrooms(request):
    all_data = [
        {'id':1,'room':'1','date':"01/08/24",'image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACFSURBVHgBXVBJEsMwCBMe//+xIVxLWUSc9sAwgAQScgEfE4ECMPfKEXJHZniErCw0ANaAJvSwspGwE50N7W0yGyYrwZuNnzN2es5LvsnCHxizbfpLD7ODxqgRynq/NeXgamPlugis9+MumAma83T/1Gs0vEClL4k0dt7Ds/OScnk3cf6JL1E8ilsFjEzgAAAAAElFTkSuQmCC'},
        {'id':2,'room':'2','date':"01/08/24",'image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACkSURBVHgBTVDbDkMhCIPF/0/2qweNl4c5WiDbg0G0LS36vOUztootkbEuq23R7jXP7d43Nvs6yMGTIBnbP5coqh8SGtDDWTZd7VCJClWdfMcBcJIt3RvedyjFpAABTEU76WenpyCqhSrfGzxBaYQ3YTB4zt6mMkOrcVDCx7MIYmqroEydKaEEUK0k05el+6p9/YEkAqnkin7rybG1EmEIEDM9wF93oeMQPWy5kgAAAABJRU5ErkJggg=='},
        {'id':3,'room':'3','date':"01/08/24",'image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAClSURBVHgBVVFRFsMgDAKfd9j9j7jqPicLifatX6kECEmJ92txChpCi4qoHCLHym+MpTbB/iBd0XSdEkyeS/wg8Y4BNjfiwVDagYEhSLhElWMQEwiSlZvEIjmCQpx4b6FCPO5Mm+RcdnMUx+uZ6Q/YTpnVI7UNIuP3zlRjUsAirxTdWzOX0TnH2bomlLtaEs64sbCF5ZgnKnK3rRVu7uq7HUftH4AfLRrQA32ZT/gAAAAASUVORK5CYII='}
    ]
    context = {'classrooms':all_data}
    return render(request,'app_classroom/classrooms.html',context)

def classroom(request,classroom_id):
    print("classroom input id:",classroom_id)
    context = {'num':classroom_id}
    return render(request, 'app_classroom/classroom.html',context)