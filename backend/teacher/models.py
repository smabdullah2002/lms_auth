from django.db import models
from _applib.model_choices_field import GenderChoice, status

class TeacherModel(models.Model):
    phone_number = models.CharField(max_length=14, unique=True)
    full_name= models.CharField(max_length=100)
    profile_picture= models.CharField(max_length=300)
    gender=models.CharField(max_length=10, choices=GenderChoice.choices, default=GenderChoice.OTHER)
    website=models.CharField(max_length=100, blank=True, null=True)
    password=models.CharField(max_length=300, blank=False, null=False)
    status=models.CharField(max_length=10, choices=status.choices, default=status.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.phone_number
    
    
    class Meta:
        verbose_name= "Teacher"
        verbose_name_plural= "Teachers"
        db_table= "teachers"