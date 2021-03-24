from django.http.response import JsonResponse
from Apps import Alumnos
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView

# models
from Apps.Alumnos.models import Alumno
# forms
from Apps.Alumnos.forms import AlumnoForm, ApoderadoForm, ApoderadoSecundarioForm, ObservacionForm

# Create your views here.


class AlumnosList(ListView):
    model = Alumno
    template_name = 'Alumnos/alumnos_registrados.html'
    context_object_name = 'alumnos'
    queryset = Alumno.objects.filter(
        status_student=True)


class AlumnosCreate(CreateView):
    model = Alumno
    template_name = 'Alumnos/alumnos_form.html'
    context_object_name = 'alumnos'
    form_class = AlumnoForm

    def get_context_data(self, **kwargs):
        context = super(AlumnosCreate, self).get_context_data(**kwargs)
        context['form2'] = ApoderadoForm()
        context['form3'] = ApoderadoSecundarioForm()
        context['form4'] = ObservacionForm()
        return context
        

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                Alumno = CreateAlumno(form)
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = " "
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('alumnos: list')

    def CreateAlumno(self, form):
        form.cleaned_data.get('')
        pass

    def CreateParents(self):
        pass

    def CreateObservation(self):
        pass
