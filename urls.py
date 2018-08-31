"""embutidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from app.views import *
from app.Views.ventaView import *
from app.Views.productoView import *
from app.Views.cajaView import *
from app.Views.reporteView import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', nuevaVenta),
    url(r'^login/$', Login),
    url(r'^logout/$', Logout),
    url(r'^home/$', nuevaVenta),
    ################## VENTA ##############################
    url(r'^venta/$', nuevaVenta),
    url(r'^venta/nuevo/$', nuevaVenta),
    url(r'^venta/insertar/$', insertarVenta),
    url(r'^venta/imprimir/$', imprimirVenta),
    url(r'^venta/anular/$', anularVenta),
    url(r'^venta/imprimir/(?P<id_venta>\d+)/$', imprimirVentaGET),
    url(r'^venta/listar', login_required(VentaList.as_view()), name='mascota_listar'),

    ################## PRODUCTO ########################
    url(r'^producto/nuevo/$', nuevoProducto),
    url(r'^producto/detalle/$', nuevoProducto),
    url(r'^producto/editar/$', nuevoProducto),
    #url(r'^producto/listar/$', listarProducto),
    url(r'^producto/buscar/$', BuscarProducto),
    url(r'^producto/listar', login_required(ProductoList.as_view()), name='mascota_listar'),
    ################## REPORTES ###########################(?P<pk>\d+)/
    url(r'^reporte/venta/$', reporteVenta),
    url(r'^reporte/caja/$', reporteCierreCaja),
    url(r'^reporte/venta/$', reporteVenta),


    ################## CAJA ###############################
    url(r'^caja/apertura/$', registrarAperturacaja),
    url(r'^caja/cierre/$', registrarCierrecaja),
    #url(r'^Caja/movimiento/$', registrarOperacion),

    
]
