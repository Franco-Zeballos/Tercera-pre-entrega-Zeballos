from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    comision = forms.IntegerField()
    
class ProfeFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    edad = forms.IntegerField()
    
class FamiliarFormulario(forms.Form):
    parentesco = forms.CharField()
    nombre = forms.CharField()
    edad = forms.IntegerField()
    fecha = forms.DateField()
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido =forms.CharField()
    camada = forms.IntegerField()
    cumple = forms.DateField()
    
class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()
    
    
