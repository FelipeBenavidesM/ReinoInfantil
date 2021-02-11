from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy
# models
from Apps.Profesores.models import Profesor

# forms
from Apps.Profesores.forms import ProfesorForm

# Create your views here.


class ProfesorList(ListView):
    model = Profesor
    template_name = 'Profesores/profesores_registrados.html'
    context_object_name = 'profesores'
    queryset = Profesor.objects.filter(status_teacher=True)


class ProfesorCreate(CreateView):
    model = Profesor
    template_name = 'Profesores/profesor_form.html'
    form_class = ProfesorForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                new_teacher = Profesor(
                    rut_teacher=form.cleaned_data.get('rut_teacher'),
                    first_name_teacher=form.cleaned_data.get(
                        'first_name_teacher'),
                    last_name_teacher=form.cleaned_data.get(
                        'last_name_teacher'),
                    address_teacher=form.cleaned_data.get('address_teacher'),
                    phone_number_teacher=form.cleaned_data.get(
                        'phone_number_teacher'),
                    email_teacher=form.cleaned_data.get('email_teacher'),
                )
                new_teacher.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = " "
                error = form.errors

                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('educadoras: list')


class ProfesorUpdate(UpdateView):
    model = Profesor
    template_name = 'Profesores/profesor_formulario.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('educadoras:list')


class ProfesorDelete(DeleteView):
    model = Profesor
    template_name = 'Profesores/profesor_delete.html'
    context_object_name = 'profesor'
    success_url = reverse_lazy('educadoras:list')

    def post(self, request, pk, *args, **kwars):
        object = Profesor.objects.get(pk=pk)
        object.status_teacher = False
        object.save()
        return redirect('educadoras:list')
