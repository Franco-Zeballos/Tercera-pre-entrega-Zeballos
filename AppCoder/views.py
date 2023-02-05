from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def estudiantes(request):
    
    return render(request, "AppCoder/estudiantes.html")

def profesores(request):
    
    return render(request, "AppCoder/profesores.html")

def entregables(request):
    
    return render(request, "AppCoder/entregables.html")

def cursos(request):
    
    return render(request, "AppCoder/cursos.html")

def cursoFormulario(request):
    
    if request.method == "POST":
        
        formulario1 = CursoFormulario(request.POST)
        
        if formulario1.is_valid():
            
            info = formulario1.cleaned_data
            
            curso = Curso(nombre=info["nombre"], camada=info["camada"], comision=info["comision"])
        
            curso.save()
        
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        formulario1 = CursoFormulario()
    
    return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario1})

def busquedaCamada(request):
    
    return render(request, "AppCoder/inicio.html")

def resultados(request):
    
    if request.GET["camada"]:
        
        camada=request.GET["camada"]
        
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, "AppCoder/inicio.html",{"cursos":cursos, "camada":camada})
    
    else:
        
        respuesta = "No enviaste datos."
    
    return HttpResponse(respuesta)
 
def profeFormulario(request):
    
    if request.method == "POST":
        
        formularioProf = ProfeFormulario(request.POST)
        
        if formularioProf.is_valid():
            
            info = formularioProf.cleaned_data
            
            prof = Profesor(nombre=info["nombre"],
                        apellido=info["apellido"],
                        email=info["email"],
                        profesion=info["profesion"],
                        edad=info["edad"])
            prof.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
            
            formularioProf = ProfeFormulario()
        
    return render(request, "AppCoder/profeFormulario.html", {"form2":formularioProf})
                
def famFormulario(request):
    
    if request.method == "POST":
        
        formularioFam =  FamiliarFormulario(request.POST)
        
        if formularioFam.is_valid():
            
            info = formularioFam.cleaned_data
            
            fam = Familiar(parentesco=info["parentesco"], 
                        nombre=info["nombre"],
                        edad=info["edad"],
                        fecha=info["fecha"])
            fam.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        
        formularioFam = FamiliarFormulario()
    
    return render(request, "AppCoder/famFormulario.html", {"form3":formularioFam})

def estudianteFormulario(request):
    
    if request.method == "POST":
        
        formularioEstudiante =  EstudianteFormulario(request.POST)
        
        if formularioEstudiante.is_valid():
            
            info = formularioEstudiante.cleaned_data
            
            Est = Estudiante( 
                        nombre=info["nombre"],
                        apellido=info["apellido"],
                        camada=info["camada"],
                        cumple=info["cumple"],)
            Est.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        
        formularioEstudiante = EstudianteFormulario()
    
    return render(request, "AppCoder/estudianteFormulario.html", {"form4":formularioEstudiante})

def entFormulario (request):
    
    if request.method == "POST":
        
        formularioEnt = EntregableFormulario(request.POST)
        
        if formularioEnt.is_valid():
            
            info = formularioEnt.cleaned_data
            
            Ent = Entregable(nombre=info["nombre"],
                             fechaDeEntrega=info["fechaDeEntrega"],
                             entregado=info["entregado"],)
                             
            Ent.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
            
        formularioEnt = EntregableFormulario()
            
    return render(request, "AppCoder/entFormulario.html", {"form5":formularioEnt})    