from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.



class StaffProfile(models.Model):
    DIRECTORATE_CHOICES = [
            ('Clinical_Services', 'Clinical Services'),
            ('Nursing_Services', 'Nursing Services'),
            ('Training, Research & Innovations', 'Training, Research & Innovations'),
            ('IMIC', 'IMIC'),
            ('Human_Resource_Development', 'Human Resource Development'),
            ('Planning, Strategy & Development', 'Planning, Strategy & Development'),
            ('Partnerships_Linkages_&_Resource_Mobilisation', 'Partnerships, Linkages & Resource Mobilisation'),
        ]

    pf_number = models.CharField(max_length=100, blank=True)
    names = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    directorate = models.CharField(choices=DIRECTORATE_CHOICES,max_length=100, blank=True)
    status = models.BooleanField(default=False)
    images = models.ImageField(upload_to='staff_pics', default='default.jpg')
    
    
    def __str__(self):
       return f'{self.names} Details'
   
    def save(self):
        super().save()

        img = Image.open(self.images.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.images.path)
   
class TISNStudentProfile(models.Model):
    COURSE_CHOICES = [
            ('Oncology Nursing', 'Oncology Nursing'),
            ('Critical Care Nursing', 'Critical Care Nursing'),
        ]
    admission_number = models.CharField(max_length=100, blank=True)
    names = models.CharField(max_length=100, blank=True)
    course = models.CharField(choices=COURSE_CHOICES, max_length=100, blank=True)
    start_date = models.DateField(max_length=100, blank=True)
    end_date = models.DateField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    images = models.ImageField(upload_to='tisn_pics', default='default.jpg')
    
    def __str__(self):
       return f'{self.names} Details'
    
    def save(self):
        super().save()

        img = Image.open(self.images.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.images.path)

class StudentProfile(models.Model):
    DIRECTORATE_CHOICES = [
            ('Clinical_Services', 'Clinical Services'),
            ('Nursing_Services', 'Nursing Services'),
            ('Training, Research & Innovations', 'Training, Research & Innovations'),
            ('IMIC', 'IMIC'),
            ('Human_Resource_Development', 'Human Resource Development'),
            ('Planning, Strategy & Development', 'Planning, Strategy & Development'),
            ('Partnerships_Linkages_&_Resource_Mobilisation', 'Partnerships, Linkages & Resource Mobilisation'),
        ]
    trainee_number = models.CharField(max_length=100, blank=True)
    names = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    directorate = models.CharField(choices=DIRECTORATE_CHOICES, max_length=100, blank=True)
    start_date = models.DateField(max_length=100, blank=True)
    end_date = models.DateField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    images = models.ImageField(upload_to='student_pics', default='default.jpg')
    
    
    
    def __str__(self):
       return f'{self.names} Details'

    def save(self):
        super().save()

        img = Image.open(self.images.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.images.path)