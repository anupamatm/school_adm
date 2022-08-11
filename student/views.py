from django.shortcuts import render

# Create your views here.
def st_login(request):
    return render(request,'st_login.html')

def sthome(reqest):
    return render(reqest,'sthome.html')

def view_attendence(reqest):
    return render(reqest,'view_attendence.html')

def view_marks(reqest):
    return render(reqest,'view_marks.html')