from django.db import models

# Create your models here.

class Doctors(models.Model):
    dname = models.CharField(max_length=199, null=True)
    dage = models.PositiveIntegerField()
    drefno = models.PositiveIntegerField()
    dspecialist = models.CharField(max_length=199, null=True)

    def __str__(self) -> str:
        return self.dname
    
class Patients(models.Model):
    pname = models.CharField(max_length=199, null=True)
    page = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.pname


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    dayField = models.CharField(max_length=199, null = True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return self.dayField

