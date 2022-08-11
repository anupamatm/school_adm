from django.urls import path
from .import views

urlpatterns=[

   path('home',views.home, name='home'),
   path('',views.login, name='login'),
   path('student',views.student, name='student'),
   path('teacher',views.teacher, name='teacher'),
   
]