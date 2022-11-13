from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=120, blank=False)
    contact = models.CharField(max_length=20, blank=False)
    sms = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Parameter(models.Model):
    patient_name = models.CharField(max_length=120, blank=False)
    aadhaar_no = models.CharField(max_length=20, blank=False)
    temperature = models.FloatField(max_length=12)
    heart_bit = models.FloatField(max_length=12)
    spo2 = models.FloatField(max_length=12)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.patient_name