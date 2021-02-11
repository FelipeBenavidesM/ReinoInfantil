from django.db import models

# Create your models here.
class Profesor(models.Model):
    rut_teacher = models.CharField(max_length = 12, blank =False, null=False, unique = True)
    first_name_teacher = models.CharField(max_length = 75, blank =False, null=False)
    last_name_teacher = models.CharField(max_length = 75, blank =False, null=False)
    address_teacher = models.CharField(max_length = 100, blank =False, null=False)
    phone_number_teacher = models.IntegerField( null = True,blank = True)
    email_teacher = models.EmailField(max_length=150, blank = False, null = False)
    
    status_teacher = models.BooleanField(default=True)
    
    created_teacher = models.DateTimeField(auto_now_add = True)
    modified_teacher = models.DateTimeField(auto_now = True) 

    
class CursoProfesor(models.Model):
    teacher_fk = models.ForeignKey('Profesor', on_delete = models.RESTRICT)
    Course_fk = models.ForeignKey('Curso', on_delete = models.RESTRICT)
    
    created_course_teacher = models.DateTimeField(auto_now_add = True)
    modified_course_teacher = models.DateTimeField(auto_now = True)
	

class Curso(models.Model):
    grade = models.CharField(max_length = 50, blank =False, null=False, unique=True)
    
    created_course = models.DateTimeField(auto_now_add = True)
    modified_course = models.DateTimeField(auto_now = True)
	

class Recordatorio(models.Model):
    
    teacher_rec_fk = models.ForeignKey('Profesor',on_delete = models.RESTRICT)
    
    name = models.CharField(max_length = 75, blank = False, null = True)
    description = models.TextField(max_length = 200, blank= True, null=True)
    start_date = models.DateField(blank = False, null=False, auto_now = True, auto_now_add = False) 
    end_date = models.DateField(blank = False, null=False, auto_now = True, auto_now_add = False)
    alarm = models.BooleanField(default=True)
    
    created_reminder = models.DateTimeField(auto_now_add = True)
    modified_reminder = models.DateTimeField(auto_now = True)
	
    