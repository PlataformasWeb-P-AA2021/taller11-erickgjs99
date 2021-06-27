from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edificio/<int:id>', views.obtener_edificio, 
            name='obtener_edificio'),
        path('crearEdificio', views.crear_edificio, 
            name='crear_edificio'),
        path('editarEdificio/<int:id>', views.editar_edificio, 
            name='editar_edificio'),
        path('eliminarEdificio/<int:id>', views.eliminar_edificio, 
            name='eliminar_edificio'),
        # DEPARTAMENTOS
        path('crearDepartamentos', views.crear_departamento, 
            name='crear_departamento'),
        path('editarDepartamento/<int:id>', views.editar_departamento, 
            name='editar_departamento'),
        path('crearDepartamento/edificio/<int:id>', 
            views.crear_departamento_edificio, 
            name='crear_departamento_edificio'),
        path('eliminarDepartamento/<int:id>', views.eliminar_departamento, 
            name='eliminar_departamento'),
 ]