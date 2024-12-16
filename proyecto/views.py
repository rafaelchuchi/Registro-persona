from django.http import Http404, HttpResponse
from django.shortcuts import render
from biblioteca.models import Persona

def persona_reg(request):
    mensajes = []
    if request.method == 'POST':
        if not request.POST.get('vNom', ''):
            mensajes.append('Por favor ingrese nombre de usuario')
        if not request.POST.get('vApe', ''):
            mensajes.append('Por favor ingrese apellido de usuario')
        if not request.POST.get('vId', ''):
            mensajes.append('Por favor ingrese cedula identidad de usuario')
        if not request.POST.get('vSexo', ''):
            mensajes.append('Por favor ingrese sexo del usuario')
        if not request.POST.get('vFecha', ''):
            mensajes.append('Por favor ingrese fecha de nacimiento de usuario')
        if not request.POST.get('vDirec', ''):
            mensajes.append('Por favor ingrese direccion del usuario')
        if not request.POST.get('vTlf', ''):
            mensajes.append('Por favor ingrese telefono de usuario')
        if not request.POST.get('vCorreo', ''):
            mensajes.append('Por favor ingrese correo de usuario')
        if not mensajes:
            vNom = request.POST.get('vNom','')
            vApe = request.POST.get('vApe','')
            vId = request.POST.get('vId','')
            vSexo = request.POST.get('vSexo','')
            vFecha = request.POST.get('vFecha','')
            vDirec = request.POST.get('vDirec','')
            vTlf = request.POST.get('vTlf','')
            vCorreo = request.POST.get('vCorreo','')

            nvoPersona = Persona(nom=vNom, ape=vApe, idn=vId, sx=vSexo, fec=vFecha, dirc=vDirec, tel=vTlf, cor= vCorreo)
            nvoPersona.save()
            mensajes.append('Usuario ingresado')
    else:
        mensajes.append('Por favor ingrese los datos requeridos')  
        
    return render(request, 'usuario.html',{'mensajes':mensajes})

def reporte(request):
    user = Persona.objects.all()
    return render(request, "reporte1.html",{'Persona':user})