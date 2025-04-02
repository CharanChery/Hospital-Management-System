from django.db import models

# Create your models here.


class RegisterDoctor(models.Model):
    Dname=models.CharField(max_length=100)
    Dage=models.PositiveIntegerField()
    Dregid=models.IntgerField()
    Dmobno=models.IntegerField()
    Dadress=models.TextField()
    Dhosptial=models.CharField(max_length=10)
    Dmailid=models.EmailField()
    Dpassword=models.IntegerField()

    gender=models.CharField(max_length=10, choices=[('MALE','MALE'),('FEMALE','FEMALE')])


    def __str__(self):
        return self.name


class RegisterPatient(models.Model):
    Pname=models.CharField(max_length=100)
    Page=models.PositiveIntegerField()
    Phealthid=models.IntgerField()
    Padress=models.TextField()
    Pmobno=models.IntegerField()
    Pmailid=models.EmailField()
    Ppassword=models.IntegerField()

    gender=models.CharField(max_length=10, choices=[('MALE','MALE'),('FEMALE','FEMALE')])

    def __str__(self):
        return self.name