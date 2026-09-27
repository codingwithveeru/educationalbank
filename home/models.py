
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='courses/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User  # ← Ye line add kar

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ← Line 31
    course = models.CharField(max_length=200)
    certificate_id = models.CharField(max_length=50, unique=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.course}" 

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default='EduMaster')
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()             