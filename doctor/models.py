from django.db import models
from userauths import models as userauths_model
from django.utils import timezone


class Doctor(models.Model):
  user = models.OneToOneField(userauths_model.User,on_delete = models.CASCADE)
  image = models.FileField(upload_to= "images",null=True,blank=True)
  full_name = models.CharField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=100, null=True, blank=True)
  country = models.CharField(max_length=100, null=True, blank=True)
  bio_data = models.CharField(max_length=100, null=True, blank=True)
  specialization = models.CharField(max_length=100, null=True, blank=True)
  qualification = models.CharField(max_length=100, null=True, blank=True)
  year_of_experience = models.CharField(max_length=100, null=True, blank=True)
  next_available_appointment_date = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return f"DR.{self.full_name}"
  
class Notification(models.Model):

  NOTIFICATION_TYPE = (
    ('New_Appointment','New_Appointment'),
    ('Appointment_Cancelled','Appointment_Cancelled')
  ) 
  doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True,blank=True)

  appointment = models.ForeignKey('Base.Appointment', on_delete=models.CASCADE,null=True,blank=True,related_name = 'doctor_appointment_Notification') 
  type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)
  seen = models.DateField(auto_now_add=True)
   
  class Meta:
    verbose_name_plural = "Notification" 

  def __str__(self) -> str:
    return f"DR.{self.doctor.full_name} Notification"





