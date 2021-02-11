# Django
from django import forms

# Models
from Apps.Profesores.models import Profesor


class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ['rut_teacher', 'first_name_teacher', 'last_name_teacher',
                  'address_teacher', 'phone_number_teacher', 'email_teacher']
        labels = {
            'rut_teacher': 'Rut ',
            'first_name_teacher': ' Nombres ',
            'last_name_teacher': 'Apellidos ',
            'address_teacher': 'Dirección ',
            'phone_number_teacher': 'Número Celular ',
            'email_teacher': 'Correo Electrónico',
        }
        widgets = {
            'rut_teacher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'inputRut',
                    'placeholder': '11222333-9'
                }),

            'first_name_teacher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'inputFirstName'
                }),

            'last_name_teacher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'inputLastName'
                }),

            'address_teacher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'inputAddress'
                }),

            'phone_number_teacher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'inputPhoneNumber'
                }),

            'email_teacher': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'inputEmail'
                }),
        }
