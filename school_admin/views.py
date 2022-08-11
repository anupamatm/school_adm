from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'admin_login.html')

def home(request):
    return render(request,'admin_home.html')


def student(request):
    return render(request,'view_student.html')

def teacher(request):
    return render(request,'view_teacher.html')