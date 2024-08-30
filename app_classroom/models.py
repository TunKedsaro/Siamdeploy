from django.db import models

# {'id':4,'room':2,'date':datetime(2024,8,2),'time':'121000','image':'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAClSURBVHgBVVFRFsMgDAKfd9j9j7jqPicLifatX6kECEmJ92txChpCi4qoHCLHym+MpTbB/iBd0XSdEkyeS/wg8Y4BNjfiwVDagYEhSLhElWMQEwiSlZvEIjmCQpx4b6FCPO5Mm+RcdnMUx+uZ6Q/YTpnVI7UNIuP3zlRjUsAirxTdWzOX0TnH2bomlLtaEs64sbCF5ZgnKnK3rRVu7uq7HUftH4AfLRrQA32ZT/gAAAAASUVORK5CYII='},
# Create your models here.
class Student(models.Model):
    room = models.CharField(max_length=20)
    date = models.DateTimeField(null=True)
    image = models.TextField()  # Using TextField