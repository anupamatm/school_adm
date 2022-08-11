from django.urls import path
from .import views

urlpatterns=[
   
   path('attendence/',views.attendence, name='attendence'),
   path('marks/',views.marks, name='marks'),
   path('students/',views.students, name='students'),
   path('t_home/',views.t_home, name='t_home'),
   
]