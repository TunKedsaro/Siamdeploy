from django.urls import path
from app_general import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('realtime',views.realtime,name='realtime'),
    path('uploadimage',views.upload_image,name='upload_image'),
    path('videoextract',views.video_extract,name='video_extract'),
]
