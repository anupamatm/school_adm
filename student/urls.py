from django.urls import path
from .import views

urlpatterns=[
   
   path('st_login/',views.st_login, name='st_login'),
   path('view_marks/',views.view_marks, name='view_marks'),
   path('view_attendence/',views.view_attendence, name='view_attendence'),
   path('sthome/',views.sthome,name='sthome')

]