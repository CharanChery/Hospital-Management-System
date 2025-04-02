from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *


# Create your views here.

def Maindashboard(req):
    return render(req, 'DoctorDashboard.html', {})


def EditAvail(req):
    editForm = AvailabilityForm()

    if req.method == "POST":
        editForm = AvailabilityForm(req.POST, req.FILES)
        if editForm.is_valid():
            availability = editForm.save(commit=False)
            doctor_id = req.POST.get('doctor')
            if doctor_id:
                doctor = get_object_or_404(Doctors, id=doctor_id)
                availability.doctor = doctor
            else:
                return render(req, 'EditAvailability.html', {
                    'forms': editForm,
                    'error': 'Doctor must be selected.'
                })
            availability.save()
            editForm = AvailabilityForm()
        else:
            return render(req, 'EditAvailability.html', {'forms': editForm})
    else:
        return render(req, 'EditAvailability.html', {'forms': editForm})

    return render(req, 'EditAvailability.html', {'forms': editForm})
