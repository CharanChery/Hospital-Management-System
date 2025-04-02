from django import forms
from .models import *


class RegisterDoctorForm(forms.Form):
    class Meta:
        models = RegisterDoctor
        fields = "__all__"



class RegisterPatientForm(forms.Form):
    class Meta:
        models = RegisterPatient
        fields = "__all__"