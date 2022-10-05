from django.urls import path, include
from .views import * #importa todas las vistas
from rest_framework import routers #para importar los serializers creados y ser vistos

router = routers.DefaultRouter()#permite crear urls para las api
router.register('Checkin', CheckInViewset),
router.register('Checkout', CheckOutViewset),
router.register('Cliente', ClienteViewset),
router.register('Departamento', DepartamentoViewset), ####
router.register('Acompaniante', AcompanianteViewset),
router.register('Ciudad', CiudadViewset),
router.register('Comuna', ComunaViewset),
router.register('Conductor', ConductorViewset),
router.register('serve_extra', ServicioextraViewset),
router.register('tour', TourViewset),
router.register('Funcionario', FuncionarioViewset),
router.register('Reserva', ReservaViewset),
router.register('Mantenimiento', MantenimientoViewset),
router.register('Multa', MultaViewset),
router.register('Pago', PagoViewset),
router.register('Region', RegionViewset),
router.register('Vehiculo', VehiculoViewset),



urlpatterns = [
    path('', home, name="home"),
    path('ciudad/', listar_ciudad, name="listar_ciudad"),
    path('api/', include(router.urls)),
    path('registro/', registro, name="registro"),
    #path('departamento/',DepartamentoView.as_view(), name='departamento_list')
    path('departamento/', departamento_list),
    path('departamento/<id>', departamento_list_id),
    path('departamento/crear/', departamento_create),
    path('departamento/modificar/<id>', departamento_modify),
    path('departamento/eliminar/<id>', departamento_delete),
    path('region/', region),
    #Usuarios
    path('usuario/crear/', usuario_create),
    path('usuario/<id>', get_usuario),
    path('usuario/modificar/<id>', modificar_usuario),
]
