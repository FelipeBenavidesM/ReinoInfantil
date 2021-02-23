from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.db.models import Q
# models
from Apps.Profesores.models import Profesor

# forms
from Apps.Profesores.forms import ProfesorForm

# Create your views here.


class ProfesorList(ListView):
    model = Profesor
    template_name = 'Profesores/profesores_registrados.html'
    context_object_name = 'profesores'
    queryset = Profesor.objects.filter(status_teacher=True).order_by('-created_teacher')

class ProfesorFilter(ListView):
    model = Profesor
    
    def get(self, request, *args, **kwargs):
        result = request.GET.get('buscar')
        query = Profesor.objects.filter(Q(status_teacher=True),
        Q(rut_teacher = result) | Q(first_name_teacher = result) | Q(last_name_teacher = result))
        return render(request,'Profesores/profesores_registrados.html',{'profesores': query})

class ProfesorCreate(CreateView):
    model = Profesor
    template_name = 'Profesores/profesor_form.html'
    context_object_name = 'profesor'
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
    template_name = 'Profesores/profesor_form.html'
    form_class = ProfesorForm
    
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('educadoras: list')

class ProfesorDelete(DeleteView):
    model = Profesor
    template_name = 'Profesores/profesor_delete.html'
    context_object_name = 'profesor'
    success_url = reverse_lazy('educadoras:list')


    def delete(self,request,pk,*args,**kwars):
        if request.is_ajax():
            profesor = self.get_object()
            profesor.status_teacher = False
            profesor.save()

            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response

        return redirect('educadoras:list')
