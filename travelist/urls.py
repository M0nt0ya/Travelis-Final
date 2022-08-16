"""travelist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sistema.views import index, login, asientos, hora, horarios, opinion, recuperacion, pago_Tarjeta, metodos, opiniones, registros, datos_Tarjeta, horarios_Admin, recuperaciones_Admin, perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include('sistema.urls')),
    path('registros_Admin/', registros),
    path('', index),
    path('login/', login),
    path('horarios/', horarios),
    path('horarios_Admin/', horarios_Admin),
    path('hora/', hora),
    path('asientos/', asientos),
    path('perfil/', perfil),
    path('opinion/', opinion),
    path('opinion_Admin/', opiniones),
    path('recuperacion/', recuperacion),
    path('recuperaciones_Admin/', recuperaciones_Admin),
    path('pago_Tarjeta/', pago_Tarjeta),
    path('pago_Tarjeta_Admin/', datos_Tarjeta),
    path('metodos/', metodos)
]
