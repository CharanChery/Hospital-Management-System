from django import forms
from .models import *


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = DoctorAvailability
        fields = ['doctor','dayField', 'start_time', 'end_time']
        widgets = {
            'doctor': forms.Select(attrs={"class": "form-control"}),
            'dayField': forms.Select(  # Use forms.Select for choices
                choices=[("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"),
                         ("Thursday", "Thursday"), ("Friday", "Friday"), ("Saturday", "Saturday")],
                attrs={"class": "form-control"}
            ),


            'start_time': forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            'end_time': forms.TimeInput(attrs={"type": "time", "class": "form-control"})
        }
