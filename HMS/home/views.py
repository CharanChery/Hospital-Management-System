from django.shortcuts import render

# Create your views here.

def Registration(request):
    result = request.get('data')
    print(result)
    if result == 'Patient':
        pass
    elif result == 'Doctor':
        pass
    return render(request, 'Registration.html')

def loginView(request):
    
    return render(request,"login.html",{})



def registerView(request):
    return render(request,"regester.html",{})



