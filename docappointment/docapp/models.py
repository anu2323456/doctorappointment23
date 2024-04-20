from django.db import models

# Create your models here.

class Doctors(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    speciality=models.CharField(max_length=250)
    availability=models.BooleanField(default=False)

    def __str__(self):
     return self.name
    

class Docappontment(models.Model):
   doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE,null=True)
   time=models.TimeField()
   date=models.DateField()
   Patientname=models.CharField(max_length=250)


   
   def __str__(self):
        return f"{self.date} - {self.time} with Dr. {self.doctor.name}" if self.doctor else f"{self.date} - {self.time} (No doctor assigned)"

