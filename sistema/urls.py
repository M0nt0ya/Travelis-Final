from django.urls import path
from .views import registro, registros, guardar, index, login, asientos, hora, horarios, guardar_horarios, opinion, guardar_opiniones, recuperacion, guardar_recuperaciones, pago_Tarjeta, guardar_Datos_Tarjeta, metodos, opiniones, borrar_opiniones, datos_Tarjeta, borrar_Datos_Tarjeta, horarios_Admin, recuperaciones_Admin, borrar_registro, borrar_horarios, borrar_recuperaciones, editar_recuperaciones, editar_recuperaciones_Admin, editar_registros, editar_registros_Admin, perfil

urlpatterns = [
    # registro
    path('', registro, name='registro'),
    path('nuevo_registro/', guardar, name='guardar'),
    path('registro_Admin/', registros, name='registro_Admin'),
    path('borrar_registro/<int:registros_id>/', borrar_registro, name='borrar_registro'),
    path('editar_registros/', editar_registros, name='editar_registros'),
    path('editar_registros_Admin/<int:registros_id>/', editar_registros_Admin, name='editar_registros_Admin'),
    # index
    path('index/', index, name='index'),
    #login
    path('login/', login, name='login'),
    #horarios
    path('horarios/', horarios, name='horarios'),
    path('nuevo_horario/', guardar_horarios, name='guardar_horarios'),
    path('horarios_Admin/', horarios_Admin, name='horarios_Admin'),
    path('borrar_horarios/<int:destino_id>/', borrar_horarios, name='borrar_horarios'),
    #hora
    path('hora/', hora, name='hora'),
    #asientos
    path('asientos/', asientos, name='asientos'),
    #opinion
    path('opinion/', opinion, name='opinion'),
    path('opinion_Admin/', opiniones, name='opinion_Admin'),
    path('nueva_opinion/', guardar_opiniones, name='guardar_opiniones'),
    path('borrar_opinion/<int:opiniones_id>/', borrar_opiniones, name='borrar_opiniones'),
    #recuperacion
    path('recuperacion/', recuperacion, name='recuperacion'),
    path('recuperaciones_Admin/', recuperaciones_Admin, name='recuperaciones_Admin'),
    path('nueva_recuperacion/', guardar_recuperaciones, name='guardar_recuperaciones'),
    path('borrar_recuperacion/<int:recuperaciones_id>/', borrar_recuperaciones, name='borrar_recuperaciones'),
    path('editar_recuperaciones/', editar_recuperaciones, name='editar_recuperaciones'),
    path('editar_recuperaciones_Admin/<int:recuperaciones_id>/', editar_recuperaciones_Admin, name='editar_recuperaciones_Admin'),
    #tarjeta
    path('pago_Tarjeta/', pago_Tarjeta, name='pago_Tarjeta'),
    path('nuevo_Datos_Tarjeta/', guardar_Datos_Tarjeta, name='guardar_Datos_Tarjeta'),
    path('pago_Tarjeta_Admin/', datos_Tarjeta, name='pago_Tarjeta_Admin'),
    path('borrar_pago_Tarjeta/<int:datos_Tarjetas_id>/', borrar_Datos_Tarjeta, name='borrar_Datos_Tarjeta'),
    #metodos
    path('metodos/', metodos, name='metodos'),
    #perfil
    path('perfil/', perfil, name='perfil'),
]