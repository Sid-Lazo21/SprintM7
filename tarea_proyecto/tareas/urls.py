from django.urls import path
from . import views

urlpatterns = [
    # Vista para crear una nueva tarea
    path('crear/', views.CrearTareaView.as_view(), name='crear_tarea'),

    # Vista para ver los detalles de una tarea
    path('ver/<int:pk>/', views.VerTareaView.as_view(), name='ver_tarea'),

    # Vista para editar una tarea existente
    path('editar/<int:pk>/', views.EditarTareaView.as_view(), name='editar_tarea'),

    # Vista para listar todas las tareas
    path('listar/', views.ListarTareasView.as_view(), name='listar_tareas'),

    path('', views.index, name='index'),

]




