from django.urls import include, path
from AppCoder.views import *

urlpatterns = [    

    path("estudiantes/", estudiantes),
    path("profesores/", profesores, name="Profesores"),
    path("cursos/", cursos),
    path("entregables/", entregables),
    path("inicio/", inicio),
    
    
    path("cursoFormulario/", cursoFormulario, name="FormularioCurso"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("profeFormulario/", profeFormulario, name="ProfeFormulario"),
    path("famFormulario/", famFormulario, name="famiFormulario"),
    path("estudianteFormulario/", estudianteFormulario, name="estuFormulario"),   # PRIMERO VA LA URL(STRING), SEGUNDO LA FUNCION (DEF), TERCERO UN NOMBRE Q NO SE PARA K ESxd PROBE Y NO ME AFECTA NI ME ROMPE NADA
    path("entregableFormulario/", entFormulario, name="formularioEnt"), 
]