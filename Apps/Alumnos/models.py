from django.db import models
#models
from Apps.Profesores.models import Curso

class CursoAlumno(models.Model):
    course_student_fk = models.ForeignKey('Alumno', on_delete = models.RESTRICT)
    course_fk = models.ForeignKey(Curso, on_delete = models.RESTRICT)

    status_course_student = models.BooleanField(default=True)
    
    created_course_student = models.DateTimeField(auto_now_add = True)
    modified_course_student = models.DateTimeField(auto_now = True) 


class Alumno(models.Model):
    rut_student = models.CharField(max_length= 12, blank=False, null=False, unique=True)
    first_name_student = models.CharField(max_length= 75, blank=False, null=False)
    last_name_student = models.CharField(max_length= 75, blank=False, null=False)
    Date_birth_student = models.DateField(max_length= 75, blank=False, null=False)
    phone_number_emergency_student = models.IntegerField(blank=True, null=False)


    status_student = models.BooleanField(default=True)
    
    created_student = models.DateTimeField(auto_now_add = True)
    modified_student = models.DateTimeField(auto_now = True) 


class AlumnoApoderado(models.Model):
    student_fk = models.ForeignKey('Alumno', on_delete = models.RESTRICT)
    parents_fk = models.ForeignKey('Apoderado', on_delete = models.RESTRICT)
    type_fk = models.ForeignKey('TipoApoderado', on_delete = models.RESTRICT)

    status_student_parents = models.BooleanField(default=True)
    
    created_student_parents = models.DateTimeField(auto_now_add = True)
    modified_student_parents = models.DateTimeField(auto_now = True)


class  TipoApoderado(models.Model):
    name = models.CharField(max_length= 50, blank=False, null=False)

    status_type_parents = models.BooleanField(default=True)
    
    created_type_parents = models.DateTimeField(auto_now_add = True)
    modified_type_parentsy  = models.DateTimeField(auto_now = True)



class Apoderado(models.Model):
    Type_Parents_fk = models.ForeignKey('TipoApoderado', on_delete=models.RESTRICT)

    rut_parents = models.CharField(max_length = 12, blank =False, null=False, unique = True)
    first_name_parents = models.CharField(max_length = 75, blank =False, null=False)
    last_name_parents = models.CharField(max_length = 75, blank =False, null=False)
    address_parents = models.CharField(max_length = 100, blank =False, null=False)
    phone_number_parents = models.IntegerField( null = True,blank = True)
    email_parents = models.EmailField(max_length=150, blank = False, null = False)
    PickUp_child_parents = models.BooleanField(default=False)


    status_parents = models.BooleanField(default=True)
    
    created_parents = models.DateTimeField(auto_now_add = True)
    modified_parents = models.DateTimeField(auto_now = True) 


class Observaciones(models.Model):
    observation_student_fk = models.ForeignKey('Alumno', on_delete = models.RESTRICT)

    name = models.CharField(max_length = 75, blank = False, null = True)
    description = models.TextField(max_length = 200, blank= True, null=True)
    start_date = models.DateField(blank = False, null=False) 
    end_date = models.DateField(blank = False, null=False)
    alarm = models.BooleanField(default=False)

    status_observation = models.BooleanField(default=True)
    
    created_observation = models.DateTimeField(auto_now_add = True)
    modified_observation = models.DateTimeField(auto_now = True) 




