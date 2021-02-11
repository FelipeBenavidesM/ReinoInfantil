""" Profesores Urls """

# Django
from django.urls import path

# views
from Apps.Profesores import views


urlpatterns = [
    path(
        route='',
        view=views.ProfesorList.as_view(),
        name='list'
    ),

    path(
        route='Create/',
        view=views.ProfesorCreate.as_view(),
        name='create'
    ),

    path(
        route='Update/<int:pk>/',
        view=views.ProfesorUpdate.as_view(),
        name='update'
    ),

    path(
        route='Delete/<int:pk>',
        view=views.ProfesorDelete.as_view(),
        name='delete'
    ),
]
