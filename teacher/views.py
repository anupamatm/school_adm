from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def t_home(request):
    return render(request,'t_home.html')

def attendence(request):
    return render(request,'add_attendence.html')

def marks(request):
    return render(request,'add_mark.html')

def students(request):
    return render(request,'students.html')