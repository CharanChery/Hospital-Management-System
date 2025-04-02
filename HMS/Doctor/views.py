from django.shortcuts import render

# Create your views here.

def Maindashboard(req):
    return render(req, 'DoctorDashboard.html', {})
