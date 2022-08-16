from django.shortcuts import render, redirect
from .models import Registro, Destino, Opinion, Recuperacion, Datos_Tarjeta

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'html/login.html')

def asientos(request):
    return render(request, 'html/asientos.html')

def hora(request):
    return render(request, 'html/hora.html')

def horarios(request):
    return render(request, 'html/horarios.html')

def opinion(request):
    return render(request, 'html/opinion.html')

def recuperacion(request):
    return render(request, 'html/olvidaste.html')

def pago_Tarjeta(request):
    return render(request, 'html/pago.html')

def metodos(request):
    return render(request, 'html/metodos.html')

def registro(request):
    return render(request, 'html/registro.html')

def perfil(request):
    return render(request, 'html/perfil.html')

# REGISTRO

def registro(request):
    registros = Registro.objects.all()
    context = {
        "registros": registros[::-1],
        "editar_registros_Admin": None
    }
    return render(request, 'admin/registros_Admin.html', context)

def registros(request):
    registro = Registro.objects.all()
    context = {
        "registro": registro[::-1],
        "editar_registros_Admin": None
    }
    return render(request, 'admin/registros_Admin.html', context)

def borrar_registro(request, registros_id):
    registros = Registro.objects.get(id=registros_id)
    registros.delete()
    return redirect('/registros_Admin/')

def guardar(request):
    registros_nombre=request.POST['nombre']
    registros_apellido=request.POST['apellido']
    registros_usuario=request.POST['usuario']
    registros_correo_Electronico=request.POST['correo_Electronico']
    registros_contraseña=request.POST['contraseña']
    registros_repetir_Contraseña=request.POST['repetir_Contraseña']
    registros = Registro(nombre=registros_nombre, apellido=registros_apellido, usuario=registros_usuario, correo_Electronico=registros_correo_Electronico, contraseña=registros_contraseña, repetir_Contraseña=registros_repetir_Contraseña)
    registros.save()
    return redirect('/login/')

def editar_registros(request):
    registros_id=request.POST['id']
    registros_nombre=request.POST['nombre']
    registros_apellido=request.POST['apellido']
    registros_usuario=request.POST['usuario']
    registros_correo_Electronico=request.POST['correo_Electronico']
    registros_contraseña=request.POST['contraseña']
    registros_repetir_Contraseña=request.POST['repetir_Contraseña']
    registros = Registro.objects.get(pk=registros_id)
    registros.nombre = registros_nombre
    registros.apellido = registros_apellido
    registros.usuario = registros_usuario
    registros.correo_Electronico = registros_correo_Electronico
    registros.contraseña = registros_contraseña
    registros.repetir_Contraseña = registros_repetir_Contraseña
    registros.save()
    return redirect('/registros_Admin/')

def editar_registros_Admin(request, registros_id):
    registros = Registro.objects.all()
    registros_only = Registro.objects.get(pk=registros_id)
    context = {
        "registros": registros[::-1],
        "editar_registros": registros_only
    }
    return render(request, 'html/registro.html', context)

# HORARIOS

def guardar_horarios(request):
    destino = Destino(destinos=request.POST['destinos'], terminal=request.POST['terminal'], fecha_ida=request.POST['fecha_ida'], fecha_vuelta=request.POST['fecha_vuelta'])
    destino.save()
    return redirect('/hora/')

def horarios_Admin(request):
    horarios = Destino.objects.all()
    return render(request, 'admin/destinos_Admin.html', {"horarios": horarios})

def borrar_horarios(request, destino_id):
    destino = Destino.objects.get(id=destino_id)
    destino.delete()
    return redirect('/horarios_Admin/')

# OPINIONES

def guardar_opiniones(request):
    opiniones = Opinion(nombre=request.POST['nombre'], apellido=request.POST['apellido'], correo_Electronico=request.POST['correo_Electronico'], opinion=request.POST['opinion'])
    opiniones.save()
    return redirect('/opinion/')

def opiniones(request):
    opinion = Opinion.objects.all()
    return render(request, 'admin/opiniones_Admin.html', {"opinion": opinion})

def borrar_opiniones(request, opiniones_id):
    opiniones = Opinion.objects.get(id=opiniones_id)
    opiniones.delete()
    return redirect('/opinion_Admin/')

# RECUPERACION

def guardar_recuperaciones(request):
    recuperaciones_nombre = request.POST['nombre']
    recuperaciones_apellido = request.POST["apellido"]
    recuperaciones_correo_Electronico = request.POST["correo_Electronico"]
    recuperaciones = Recuperacion(nombre= recuperaciones_nombre, apellido=recuperaciones_apellido, correo_Electronico=recuperaciones_correo_Electronico)
    recuperaciones.save()
    return redirect('/recuperacion/')

def recuperaciones_Admin(request):
    recuperacion = Recuperacion.objects.all()
    context = {
        "recuperacion": recuperacion[::-1],
        "editar_recuperaciones_Admin": None
    }
    return render(request, 'admin/recuperaciones_Admin.html', context)

def borrar_recuperaciones(request, recuperaciones_id):
    recuperaciones = Recuperacion.objects.get(id=recuperaciones_id)
    recuperaciones.delete()
    return redirect('/recuperaciones_Admin/')

def editar_recuperaciones(request):
    recuperaciones_id = request.POST["id"]
    recuperaciones_nombre = request.POST["nombre"]
    recuperaciones_apellido = request.POST["apellido"]
    recuperaciones_correo_Electronico = request.POST["correo_Electronico"]
    recuperaciones = Recuperacion.objects.get(pk=recuperaciones_id)
    recuperaciones.nombre = recuperaciones_nombre
    recuperaciones.apellido = recuperaciones_apellido
    recuperaciones.correo_Electronico = recuperaciones_correo_Electronico
    recuperaciones.save()
    return redirect('/recuperaciones_Admin/')
    
def editar_recuperaciones_Admin(request, recuperaciones_id):
    recuperaciones = Recuperacion.objects.all()
    recuperaciones_only = Recuperacion.objects.get(pk=recuperaciones_id)
    context = {
        "recuperaciones": recuperaciones[::-1],
        "editar_recuperaciones": recuperaciones_only
    }
    return render(request, 'html/olvidaste.html', context)

# TARJETA

def datos_Tarjeta(request):
    datos_Tarjeta = Datos_Tarjeta.objects.all()
    return render(request, 'admin/tarjetas_Admin.html', {"datos_Tarjeta": datos_Tarjeta})

def guardar_Datos_Tarjeta(request):
    datos_Tarjetas = Datos_Tarjeta(numero_Tarjeta=request.POST['numero_Tarjeta'], nombre_Tarjeta=request.POST['nombre_Tarjeta'], mes_Expiracion=request.POST['mes_Expiracion'], anio_Expiracion=request.POST['anio_Expiracion'], CCV=request.POST['CCV'])
    datos_Tarjetas.save()
    return redirect('/pago_Tarjeta/')

def borrar_Datos_Tarjeta(request, datos_Tarjetas_id):
    datos_Tarjetas = Datos_Tarjeta.objects.get(id=datos_Tarjetas_id)
    datos_Tarjetas.delete()
    return redirect('/pago_Tarjeta_Admin/')