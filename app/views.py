from django.shortcuts import render
from .models import *
from rest_framework import viewsets, status
from .serializers import *
from .forms import * #importa todos los forms que se crean
from django.contrib.auth import authenticate, login #para autenticar al usuario
from django.db import connection #trae los procesos almacenados
from rest_framework.response import Response
from django.views import View
from rest_framework.decorators import api_view
from .procedure import *
from .tranbank import *
from django.core.mail import send_mail



# se crean clases para las api
class CheckInViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Checkin.objects.all()
    serializer_class = CheckInSerializer

class CheckOutViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Checkout.objects.all()
    serializer_class = CheckOutSerializer

class ClienteViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DepartamentoViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
class CiudadViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class ComunaViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class PagoViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class ConductorViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class FuncionarioViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ServicioextraViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Servicioextra.objects.all()
    serializer_class = ServicioextraSerializer

class TourViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class ReservaViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class MantenimientoViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

class MultaViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer

class RegionViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class VehiculoViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class AcompanianteViewset(viewsets.ModelViewSet):#este se encarga de mostrar los datos y hasta guardar
    queryset = Acompaniante.objects.all()
    serializer_class = AcompanianteSerializer

def home(request):
    return render(request, 'app/home.html')

@api_view(['GET', 'POST'])
def departamento_list(request):
    if request.method == 'GET':
        get_departamento = listar_departamento()
        if(get_departamento != []):
            departamentos = []
            res = {}
            for depa in get_departamento:
                res = {}
                res['ID_DEPTO'] = depa[0]
                res['NOM_DEPTO'] = depa[1]
                res['DESC_DEPTO'] = depa[2]
                res['DIRECCION'] = depa[3]
                res['CANT_HABITACION'] = depa[4]
                res['CANT_BANIO'] = depa[5]
                res['CALEFACCION'] = depa[6]
                res['INTERNET'] = depa[7]
                res['AMOBLADO'] = depa[8]
                res['TELEVISION'] = depa[9]
                res['DISPONIBLE'] = depa[10]
                res['VALOR_DIA'] = depa[11]
                res['COMUNA_ID_COMUNA'] = depa[12]

                departamentos.append(res)
            return Response(departamentos, status=status.HTTP_200_OK)
        elif(get_departamento == []):
            return Response({"Error": "No se encontraron departamentos"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def departamento_list_admin(request):
    if request.method == 'GET':
        get_departamento = listar_departamento_admin()
        if(get_departamento != []):
            departamentos = []
            res = {}
            for depa in get_departamento:
                res = {}
                res['NOMBRE_DEPARTAMENTO'] = depa[0]
                res['DESCRIPCION'] = depa[1]
                res['DIRECCION'] = depa[2]
                res['HABITACIONES'] = depa[3]
                res['CANTIDAD_BAÑOS'] = depa[4]
                res['CALEFACCION'] = depa[5]
                res['INTERNET'] = depa[6]
                res['AMOBLADO'] = depa[7]
                res['TELEVISION'] = depa[8]
                res['DISPONIBLE'] = depa[9]
                res['VALOR'] = depa[10]
                res['COMUNA'] = depa[11]

                departamentos.append(res)
            return Response(departamentos, status=status.HTTP_200_OK)
        elif(get_departamento == []):
            return Response({"Error": "No se encontraron departamentos"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def departamento_list_id(request,id):
    if request.method == 'GET':
        get_departamento = buscar_departamento(id)
        if(get_departamento != []):
            departamentos = []
            res = {}
            for depa in get_departamento:
                res = {}
                res['ID_DEPTO'] = depa[0]
                res['NOM_DEPTO'] = depa[1]
                res['DESC_DEPTO'] = depa[2]
                res['DIRECCION'] = depa[3]
                res['CANT_HABITACION'] = depa[4]
                res['CANT_BANIO'] = depa[5]
                res['CALEFACCION'] = depa[6]
                res['INTERNET'] = depa[7]
                res['AMOBLADO'] = depa[8]
                res['TELEVISION'] = depa[9]
                res['DISPONIBLE'] = depa[10]
                res['VALOR_DIA'] = depa[11]
                res['COMUNA_ID_COMUNA'] = depa[12]
                departamentos.append(res)
            return Response(departamentos, status=status.HTTP_200_OK)
        elif(get_departamento == []):
            return Response({"Error": "No se existen departamentos con ese ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def departamento_list_nom(request,nom):
    if request.method == 'GET':
        nombre_dep = buscar_departamento_nombre(nom)
        if(nombre_dep != []):
            departamentos = []
            res = {}
            for depa in nombre_dep:
                res = {}
                res['ID_DEPTO'] = depa[0]
                res['NOM_DEPTO'] = depa[1]
                res['DESC_DEPTO'] = depa[2]
                res['DIRECCION'] = depa[3]
                res['CANT_HABITACION'] = depa[4]
                res['CANT_BANIO'] = depa[5]
                res['CALEFACCION'] = depa[6]
                res['INTERNET'] = depa[7]
                res['AMOBLADO'] = depa[8]
                res['TELEVISION'] = depa[9]
                res['DISPONIBLE'] = depa[10]
                res['VALOR_DIA'] = depa[11]
                res['COMUNA_ID_COMUNA'] = depa[12]
                departamentos.append(res)
            return Response(departamentos, status=status.HTTP_200_OK)
        elif(nombre_dep == []):
            return Response({"Error": "No se existen departamentos con ese Nombre"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def departamento_create(request):
    if request.method == 'POST':
        nombre_dep = request.data.get('NOM_DEPTO')
        descripcion_depto = request.data.get('DESC_DEPTO')
        direccion_depto = request.data.get('DIRECCION')
        habitacion = request.data.get('CANT_HABITACION')
        banio = request.data.get('CANT_BANIO')
        calefaccion = request.data.get('CALEFACCION')
        internet = request.data.get('INTERNET')
        amoblado = request.data.get('AMOBLADO')
        television = request.data.get('TELEVISION')
        disponible = request.data.get('DISPONIBLE')
        valor_diario= request.data.get('VALOR_DIA')
        comuna_id= request.data.get('COMUNA_ID_COMUNA')
        salida = crear_departamento(nombre_dep,descripcion_depto,direccion_depto,habitacion,banio,calefaccion,internet,amoblado,television,disponible,valor_diario,comuna_id)
        if salida == 1:
            return Response({'response':'Se creo correctamente la Departamento'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


@api_view(['POST'])
def departamento_modify(request, id):
    if request.method == 'POST':
        #Primero deberiamos verificar que el departamento exista
        get_departamento = buscar_departamento(id)
        if(get_departamento == []):
            #Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe departamento con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            nombre_dep = request.data.get('NOM_DEPTO')
            descripcion_depto = request.data.get('DESC_DEPTO')
            direccion_depto = request.data.get('DIRECCION')
            habitacion = request.data.get('CANT_HABITACION')
            banio = request.data.get('CANT_BANIO')
            calefaccion = request.data.get('CALEFACCION')
            internet = request.data.get('INTERNET')
            amoblado = request.data.get('AMOBLADO')
            television = request.data.get('TELEVISION')
            disponible = request.data.get('DISPONIBLE')
            valor_diario= request.data.get('VALOR_DIA')
            comuna_id= request.data.get('COMUNA_ID_COMUNA')
        salida = modificar_departamento(id,nombre_dep,descripcion_depto,direccion_depto,habitacion,banio,calefaccion,internet,amoblado,television,disponible,valor_diario,comuna_id)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el Departamento'}, status=status.HTTP_200_OK)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)            

@api_view(['DELETE'])
def departamento_delete(request, id):
    if request.method == 'DELETE':
        get_departamento = eliminar_departamento(id)
        if(get_departamento == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe departamento con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_departamento(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente el Departamento'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def usuario_list(request):
    if request.method == 'GET':
        get_usuario = listar_usuario()
        if(get_usuario != []):
            usuarios = []
            res = {}
            for usuario in get_usuario:
                res = {}
                res['ID_USUARIO'] = usuario[0]
                res['NOM_USUARIO'] = usuario[1]
                res['CORREO_USUARIO'] = usuario[2]
                res['CONTRASENIA'] = usuario[3]
                res['ESTADO_USUARIO'] = usuario[4]
                res['TIPO_USUARIO_ID_TIPO_USUARIO'] = usuario[5]
                usuarios.append(res)
            return Response(usuarios, status=status.HTTP_200_OK)
        elif(get_usuario == []):
            return Response({"Error": "No se encontraron usuarios"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def usuario_list_admin(request):
    if request.method == 'GET':
        get_usuario = listar_usuario_admin()
        if(get_usuario != []):
            usuarios = []
            res = {}
            for usuario in get_usuario:
                res = {}
                res['NOM_USUARIO'] = usuario[0]
                res['CORREO_USUARIO'] = usuario[1]
                res['TIPO_USUARIO'] = usuario[2]
                res['ESTADO_USUARIO'] = usuario[3]
                usuarios.append(res)
            return Response(usuarios, status=status.HTTP_200_OK)
        elif(get_usuario == []):
            return Response({"Error": "No se encontraron usuarios"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def usuario_create(request):
    if request.method == 'POST':
        NOM_USUARIO = request.data.get('NOM_USUARIO')
        CORREO_USUARIO = request.data.get('CORREO_USUARIO')
        CONTRASENIA = request.data.get('CONTRASENIA')
        ESTADO_USUARIO = request.data.get('ESTADO_USUARIO')
        TIPO_USUARIO_ID_TIPO_USUARIO = request.data.get('TIPO_USUARIO_ID_TIPO_USUARIO')
        
        salida = crear_usuario(NOM_USUARIO,CORREO_USUARIO,CONTRASENIA,ESTADO_USUARIO,TIPO_USUARIO_ID_TIPO_USUARIO)
        if salida == 1:
            return Response({'response':'Se creo correctamente el usuario'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


@api_view(['POST'])
def usuario_modify(request, id):
    if request.method == 'POST':
        usuario = buscar_usuario(id)
        if(usuario == []):
            return  Response({'response':'No existe usuario con ese ID'}, status=status.HTTP_404_NOT_FOUND)

        NOM_USUARIO = request.data.get('NOM_USUARIO')
        CORREO_USUARIO = request.data.get('CORREO_USUARIO')
        CONTRASENIA = request.data.get('CONTRASENIA')
        ESTADO_USUARIO = request.data.get('ESTADO_USUARIO')
        TIPO_USUARIO_ID_TIPO_USUARIO = request.data.get('TIPO_USUARIO_ID_TIPO_USUARIO')
        
        salida = modificar_usuario(id,NOM_USUARIO,CORREO_USUARIO,CONTRASENIA,ESTADO_USUARIO,TIPO_USUARIO_ID_TIPO_USUARIO)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el usuario'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

@api_view(['GET'])
def get_usuario(request,id):
    if request.method == 'GET':
        get_usuario = buscar_usuario(id)
        if(get_usuario != []):
            usuario = []
            res = {}
            for user in get_usuario:
                res = {}
                res['ID_USUARIO'] = user[0]
                res['NOM_USUARIO'] = user[1]
                res['CORREO_USUARIO'] = user[2]
                res['CONTRASENIA'] = user[3]
                res['ESTADO_USUARIO'] = user[4]
                res['TIPO_USUARIO_ID_TIPO_USUARIO'] = user[5]

                usuario.append(res)
            return Response(usuario, status=status.HTTP_200_OK)
        elif(get_usuario == []):
            return Response({"Error": "No existe usuario con ese ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_usuario_correo(request,correo):
    if request.method == 'GET':
        get_usuario = buscar_usuario_correo(correo)
        if(get_usuario != []):
            usuario = []
            res = {}
            for user in get_usuario:
                res = {}
                res['ID_USUARIO'] = user[0]
                res['NOM_USUARIO'] = user[1]
                res['CORREO_USUARIO'] = user[2]
                res['CONTRASENIA'] = user[3]
                res['ESTADO_USUARIO'] = user[4]
                res['TIPO_USUARIO_ID_TIPO_USUARIO'] = user[5]

                usuario.append(res)
            return Response(usuario, status=status.HTTP_200_OK)
        elif(get_usuario == []):
            return Response({"Error": "No existe usuario con ese correo"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def reserva_list(request):
    if request.method == 'GET':
        get_reserva = listar_reserva()
        if(get_reserva != []):
            reservas = []
            res = {}
            for reserva in get_reserva:
                res = {}
                res['FECHA DE INGRESO'] = reserva[0]
                res['FECHA DE SALIDA'] = reserva[1]
                res['DIAS RESERVADOS'] = reserva[2]
                res['ESTADO'] = reserva[3]
                res['NOMBRE DEPTO'] = reserva[4]
                res['NOMBRE USUARIO'] = reserva[5]
                reservas.append(res)
            return Response(reservas, status=status.HTTP_200_OK)
        elif(get_reserva == []):
            return Response({"Error": "No se encontraron reservas"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def ReservaID_list(request):
    if request.method == 'GET':
        get_reservaID = listar_reservaID()
        if(get_reservaID != []):
            reservaID = []
            res = {}
            for reserva_id in get_reservaID:
                res = {}
                res['ID_RESERVA'] = reserva_id[0]
                reservaID.append(res)
            return Response(reservaID, status=status.HTTP_200_OK)
        elif(get_reservaID == []):
            return Response({"Error": "No se encontro la reserva"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])            
def reserva_bruto(request):
    if request.method == 'GET':
        get_reserva = listar_reserva_bruto()
        if(get_reserva != []):
            reservas = []
            res = {}
            for reserva in get_reserva:
                res = {}
                res['ID_RESERVA'] = reserva[0]
                res['FECHA_INGRESO'] = reserva[1]
                res['FECHA_SALIDA'] = reserva[2]
                res['CANT_DIA_RESERVA'] = reserva[3]
                res['ESTADO_RESERVA'] = reserva[4]
                res['FECHA_ESTADO_RESERVA '] = reserva[5]
                res['DEPARTAMENTO_ID_DEPARTAMENTO'] = reserva[6]
                res['USUARIO_ID_USUARIO'] = reserva[7]
                reservas.append(res)
            return Response(reservas, status=status.HTTP_200_OK)
        elif(get_reserva == []):
            return Response({"Error": "No se encontraron reservas"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def reserva_create(request):
    print('REQUEST', request.data.get('CORREO_USUARIO'))
    if request.method == 'POST':
        FECHA_INGRESO = request.data.get('FECHA_INGRESO')
        FECHA_SALIDA = request.data.get('FECHA_SALIDA')
        CANT_DIA_RESERVA = request.data.get('CANT_DIA_RESERVA')
        ESTADO_RESERVA = request.data.get('ESTADO_RESERVA')
        FECHA_ESTADO_RESERVA = request.data.get('FECHA_ESTADO_RESERVA')
        DEPARTAMENTO_ID_DEPARTAMENTO = request.data.get('DEPARTAMENTO_ID_DEPARTAMENTO')
        USUARIO_ID_USUARIO = request.data.get('USUARIO_ID_USUARIO')
        CORREO_USUARIO = request.data.get('CORREO_USUARIO')
        
        salida = crear_reserva(FECHA_INGRESO,FECHA_SALIDA,CANT_DIA_RESERVA,ESTADO_RESERVA,FECHA_ESTADO_RESERVA,DEPARTAMENTO_ID_DEPARTAMENTO,USUARIO_ID_USUARIO)
        resp = envio_correo('Reserva Exitosa', 'se creo la tremenda reserva', CORREO_USUARIO);

        if salida == 1:
            return Response({'response':'Se creo correctamente la reserva'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_reserva(request,id):
    if request.method == 'GET':
        get_reserva = buscar_reserva(id)
        if(get_reserva != []):
            reservas = []
            res = {}
            for reserva in get_reserva:
                res = {}
                res['ID_RESERVA'] = reserva[0]
                res['FECHA_INGRESO'] = reserva[1]
                res['FECHA_SALIDA'] = reserva[2]
                res['CANT_DIA_RESERVA'] = reserva[3]
                res['ESTADO_RESERVA'] = reserva[4]
                res['FECHA_ESTADO_RESERVA'] = reserva[5]
                res['DEPARTAMENTO_ID_DEPARTAMENTO'] = reserva[6]
                res['USUARIO_ID_USUARIO'] = reserva[7]
                reservas.append(res)
            return Response(reservas, status=status.HTTP_200_OK)
        elif(get_reserva == []):
            return Response({"Error": "No existe reserva con ese ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_reserva_usuario(request,id):
    if request.method == 'GET':
        get_reserva = listar_reserva_usuario(id)
        if(get_reserva != []):
            reservas = []
            res = {}
            for reserva in get_reserva:
                res = {}
                res['ID_RESERVA'] = reserva[0]
                res['FECHA_INGRESO'] = reserva[1]
                res['FECHA_SALIDA'] = reserva[2]
                res['CANT_DIA_RESERVA'] = reserva[3]
                res['ESTADO_RESERVA'] = reserva[4]
                res['NOM_DEPTO'] = reserva[5]
                reservas.append(res)
            return Response(reservas, status=status.HTTP_200_OK)
        elif(get_reserva == []):
            return Response({"Error": "No existe reserva con ese ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def reserva_modify(request, id):
    if request.method == 'POST':
        reserva = buscar_reserva(id)
        if(reserva == []):
            return  Response({'response':'No existe reserva con ese ID'}, status=status.HTTP_404_NOT_FOUND)

        FECHA_INGRESO = request.data.get('FECHA_INGRESO')
        FECHA_SALIDA = request.data.get('FECHA_SALIDA')
        CANT_DIA_RESERVA = request.data.get('CANT_DIA_RESERVA')
        ESTADO_RESERVA = request.data.get('ESTADO_RESERVA')
        FECHA_ESTADO_RESERVA = request.data.get('FECHA_ESTADO_RESERVA')
        DEPARTAMENTO_ID_DEPARTAMENTO = request.data.get('DEPARTAMENTO_ID_DEPARTAMENTO')
        USUARIO_ID_USUARIO = request.data.get('USUARIO_ID_USUARIO')
        
        salida = modificar_reserva(id,FECHA_INGRESO,FECHA_SALIDA,CANT_DIA_RESERVA,ESTADO_RESERVA,FECHA_ESTADO_RESERVA,DEPARTAMENTO_ID_DEPARTAMENTO,USUARIO_ID_USUARIO)
        if salida == 1:
            return Response({'response':'Se modifico correctamente la reserva'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def reserva_delete(request, id):
    if request.method == 'DELETE':
        get_reserva = eliminar_reserva(id)
        if(get_reserva == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe reserva con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_reserva(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente la reserva'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento Departamento
@api_view(['GET', 'POST'])            
def mttoDepartamento_list(request):
    if request.method == 'GET':
        get_mttoDepartamento = listar_mttoDepartamento()
        if(get_mttoDepartamento != []):
            mttoDepartamento = []
            res = {}
            for mttoDepto in get_mttoDepartamento:
                res = {}
                res['ID_MTTO'] = mttoDepto[0]
                res['FECHA_INGRESO'] = mttoDepto[1]
                res['FECHA_SALIDA'] = mttoDepto[2]
                res['DESCRIPCION_MTTO'] = mttoDepto[3]
                res['DISPONIBILIDAD'] = mttoDepto[4]
                res['DEPARTAMENTO_ID_DEPARTAMENTO'] = mttoDepto[5]
                mttoDepartamento.append(res)
            return Response(mttoDepartamento, status=status.HTTP_200_OK)
        elif(get_mttoDepartamento == []):
            return Response({"Error": "No se encontraron mantenciones"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def mttoDepartamento_create(request):
    if request.method == 'POST':
        FECHA_INGRESO = request.data.get('FECHA_INGRESO')
        FECHA_SALIDA = request.data.get('FECHA_SALIDA')
        DESCRIPCION_MTTO = request.data.get('DESCRIPCION_MTTO')
        DISPONIBILIDAD = request.data.get('DISPONIBILIDAD')
        DEPARTAMENTO_ID_DEPARTAMENTO = request.data.get('DEPARTAMENTO_ID_DEPARTAMENTO')
        
        salida = crear_mttoDepartamento(FECHA_INGRESO,FECHA_SALIDA,DESCRIPCION_MTTO,DISPONIBILIDAD,DEPARTAMENTO_ID_DEPARTAMENTO)
        if salida == 1:
            return Response({'response':'Se creo correctamente el mantenimiento'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_mttoDepartamento(request,id):
    if request.method == 'GET':
        get_mttoDepartamento = buscar_mttoDepartamento(id)
        if(get_mttoDepartamento != []):
            mttoDepartamento = []
            res = {}
            for mttoDepto in get_mttoDepartamento:
                res = {}
                res['ID_MTTO'] = mttoDepto[0]
                res['FECHA_INGRESO'] = mttoDepto[1]
                res['FECHA_SALIDA'] = mttoDepto[2]
                res['DESCRIPCION_MTTO'] = mttoDepto[3]
                res['DISPONIBILIDAD'] = mttoDepto[4]
                res['DEPARTAMENTO_ID_DEPARTAMENTO'] = mttoDepto[5]

                mttoDepartamento.append(res)
            return Response(mttoDepartamento, status=status.HTTP_200_OK)
        elif(get_mttoDepartamento == []):
            return Response({"Error": "No existen mantenimientos con ese ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def mttoDepartamento_modify(request, id):
    if request.method == 'POST':
        get_mttoDepartamento = buscar_mttoDepartamento(id)
        if(get_mttoDepartamento == []):
            return  Response({'response':'No existe un mantenimiento con ese ID'}, status=status.HTTP_404_NOT_FOUND)

        FECHA_INGRESO = request.data.get('FECHA_INGRESO')
        FECHA_SALIDA = request.data.get('FECHA_SALIDA')
        DESCRIPCION_MTTO = request.data.get('DESCRIPCION_MTTO')
        DISPONIBILIDAD = request.data.get('DISPONIBILIDAD')
        DEPARTAMENTO_ID_DEPARTAMENTO = request.data.get('DEPARTAMENTO_ID_DEPARTAMENTO')
        
        salida = modificar_mttoDepartamento(id,FECHA_INGRESO,FECHA_SALIDA,DESCRIPCION_MTTO,DISPONIBILIDAD,DEPARTAMENTO_ID_DEPARTAMENTO)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el mantenimiento'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def mttoDepartamento_delete(request, id):
    if request.method == 'DELETE':
        get_mttoDepartamento = eliminar_mttoDepartamento(id)
        if(get_mttoDepartamento == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe mantenciones con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_mttoDepartamento(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente la mantencion'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento Cliente
@api_view(['GET', 'POST'])
def cliente_list(request):
    if request.method == 'GET':
        get_cliente = listar_cliente()
        if(get_cliente != []):
            clientes = []
            res = {}
            for cliente in get_cliente:
                res = {}
                res['ID_CLIENTE'] = cliente[0]
                res['RUT_CLIENTE'] = cliente[1]
                res['NOM_CLIENTE'] = cliente[2]
                res['APELLIDO_PATERNO'] = cliente[3]
                res['APELLIDO_MATERNO'] = cliente[4]
                res['EDAD'] = cliente[5]
                res['NACIONALIDAD'] = cliente[6]
                res['GENERO'] = cliente[7]
                res['DIRECCION_CLIENTE'] = cliente[8]
                res['TELEFONO'] = cliente[9]
                res['EMAIL'] = cliente[10]
                res['USUARIO_ID_USUARIO'] = cliente[11]
                clientes.append(res)
            return Response(clientes, status=status.HTTP_200_OK)
        elif(get_cliente == []):
            return Response({"Error": "No se encontraron clientes"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_cliente(request,id):
    if request.method == 'GET':
        get_cliente = buscar_cliente(id)
        if(get_cliente != []):
            clientes = []
            res = {}
            for cliente in get_cliente:
                res = {}
                res['ID_CLIENTE'] = cliente[0]
                res['RUT_CLIENTE'] = cliente[1]
                res['NOM_CLIENTE'] = cliente[2]
                res['APELLIDO_PATERNO'] = cliente[3]
                res['APELLIDO_MATERNO'] = cliente[4]
                res['EDAD'] = cliente[5]
                res['NACIONALIDAD'] = cliente[6]
                res['GENERO'] = cliente[7]
                res['DIRECCION_CLIENTE'] = cliente[8]
                res['TELEFONO'] = cliente[9]
                res['EMAIL'] = cliente[10]
                res['USUARIO_ID_USUARIO'] = cliente[11]
                clientes.append(res)
            return Response(clientes, status=status.HTTP_200_OK)
        elif(get_cliente == []):
            return Response({"Error": "No se encontraron clientes"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def cliente_create(request):
    if request.method == 'POST':
        RUT_CLIENTE = request.data.get('RUT_CLIENTE')
        NOM_CLIENTE = request.data.get('NOM_CLIENTE')
        APELLIDO_PATERNO = request.data.get('APELLIDO_PATERNO')
        APELLIDO_MATERNO = request.data.get('APELLIDO_MATERNO')
        EDAD = request.data.get('EDAD')
        NACIONALIDAD = request.data.get('NACIONALIDAD')
        GENERO = request.data.get('GENERO')
        DIRECCION_CLIENTE = request.data.get('DIRECCION_CLIENTE')
        TELEFONO = request.data.get('TELEFONO')
        EMAIL = request.data.get('EMAIL')
        USUARIO_ID_USUARIO = request.data.get('USUARIO_ID_USUARIO')
        
        salida = crear_cliente(RUT_CLIENTE,NOM_CLIENTE,APELLIDO_PATERNO,APELLIDO_MATERNO,EDAD,NACIONALIDAD,GENERO,DIRECCION_CLIENTE,TELEFONO,EMAIL,USUARIO_ID_USUARIO)
        if salida == 1:
            return Response({'response':'Se creo correctamente el cliente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def cliente_modify(request, id):
    if request.method == 'POST':
        get_cliente = buscar_cliente(id)
        print (get_cliente)
        if(get_cliente == []):
            return  Response({'response':'No existe un cliente ID'}, status=status.HTTP_404_NOT_FOUND)

        RUT_CLIENTE = request.data.get('RUT_CLIENTE')
        NOM_CLIENTE = request.data.get('NOM_CLIENTE')
        APELLIDO_PATERNO = request.data.get('APELLIDO_PATERNO')
        APELLIDO_MATERNO = request.data.get('APELLIDO_MATERNO')
        EDAD = request.data.get('EDAD')
        NACIONALIDAD = request.data.get('NACIONALIDAD')
        GENERO = request.data.get('GENERO')
        DIRECCION_CLIENTE = request.data.get('DIRECCION_CLIENTE')
        TELEFONO = request.data.get('TELEFONO')
        EMAIL = request.data.get('EMAIL')
        USUARIO_ID_USUARIO = request.data.get('USUARIO_ID_USUARIO')
        
        salida = modificar_cliente(id,RUT_CLIENTE,NOM_CLIENTE,APELLIDO_PATERNO,APELLIDO_MATERNO,EDAD,NACIONALIDAD,GENERO,DIRECCION_CLIENTE,TELEFONO,EMAIL,USUARIO_ID_USUARIO)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el cliente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def cliente_delete(request, id):
    if request.method == 'DELETE':
        get_cliente = eliminar_cliente(id)
        if(get_cliente == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe mantenciones con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_cliente(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente la mantencion'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento Check-in
@api_view(['GET', 'POST'])
def checkIn_list(request):
    if request.method == 'GET':
        get_checkIn = listar_checkIn()
        if(get_checkIn != []):
            checkIn = []
            res = {}
            for check in get_checkIn:
                res = {}
                res['ID_CHECK_IN'] = check[0]
                res['FECHA_CHECK_IN'] = check[1]
                res['OBSERVACION'] = check[2]
                res['RESERVA_ID_RESERVA'] = check[3]
                checkIn.append(res)
            return Response(checkIn, status=status.HTTP_200_OK)
        elif(get_checkIn == []):
            return Response({"Error": "No se encontraron reservas"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def checkIn_create(request):
    if request.method == 'POST':
        FECHA_CHECK_IN = request.data.get('FECHA_CHECK_IN')
        OBSERVACION = request.data.get('OBSERVACION')
        RESERVA_ID_RESERVA = request.data.get('RESERVA_ID_RESERVA')
        
        salida = crear_checkIn(FECHA_CHECK_IN,OBSERVACION,RESERVA_ID_RESERVA)
        if salida == 1:
            return Response({'response':'Se creo correctamente el check-In'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_checkIn(request,id):
    if request.method == 'GET':
        get_checkIn = buscar_checkIn(id)
        if(get_checkIn != []):
            checkIn = []
            res = {}
            for check in get_checkIn:
                res = {}
                res['ID_CHECK_IN'] = check[0]
                res['FECHA_CHECK_IN'] = check[1]
                res['OBSERVACION'] = check[2]
                res['RESERVA_ID_RESERVA'] = check[3]
                checkIn.append(res)
            return Response(checkIn, status=status.HTTP_200_OK)
        elif(get_checkIn == []):
            return Response({"Error": "No se encontraron check-In"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def checkIn_modify(request, id):
    if request.method == 'POST':
        get_checkIn = buscar_checkIn(id)
        if(get_checkIn == []):
            return  Response({'response':'No existe un Check-In'}, status=status.HTTP_404_NOT_FOUND)

        FECHA_CHECK_IN = request.data.get('FECHA_CHECK_IN')
        OBSERVACION = request.data.get('OBSERVACION')
        RESERVA_ID_RESERVA = request.data.get('RESERVA_ID_RESERVA')
        
        salida = modificar_checkIn(id,FECHA_CHECK_IN,OBSERVACION,RESERVA_ID_RESERVA)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el Check-in'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def checkIn_delete(request, id):
    if request.method == 'DELETE':
        get_checkIn = eliminar_checkIn(id)
        if(get_checkIn == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe check-in con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_checkIn(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente el check-in'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento Inventario
@api_view(['GET', 'POST'])
def inventario_list(request):
    if request.method == 'GET':
        get_inventario = listar_inventario()
        if(get_inventario != []):
            inventarios = []
            res = {}
            for invent in get_inventario:
                res = {}
                res['ID_INVENTARIO'] = invent[0]
                res['FECHA_INVENTARIO'] = invent[1]
                res['CANT_PRODUCTO_INVENTARIO'] = invent[2]
                res['VALOR_ESTIMADO'] = invent[3]
                res['DESCRIPCION_INVENTARIO'] = invent[4]
                res['DEPARTAMENTO_ID_DEPARTAMENTO'] = invent[5]
                res['PRODUCTO_ID_PRODUCTO'] = invent[6]
                inventarios.append(res)
            return Response(inventarios, status=status.HTTP_200_OK)
        elif(get_inventario == []):
            return Response({"Error": "No se encontraron inventarios"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def inventario_create(request):
    if request.method == 'POST':
        FECHA_INVENTARIO = request.data.get('FECHA_INVENTARIO')
        CANT_PRODUCTO_INVENTARIO = request.data.get('CANT_PRODUCTO_INVENTARIO')
        VALOR_ESTIMADO = request.data.get('VALOR_ESTIMADO')
        DESCRIPCION_INVENTARIO = request.data.get('DESCRIPCION_INVENTARIO')
        DEPARTAMENTO_ID_DEPARTAMENTO = request.data.get('DEPARTAMENTO_ID_DEPARTAMENTO')
        PRODUCTO_ID_PRODUCTO = request.data.get('PRODUCTO_ID_PRODUCTO')
        
        salida = crear_inventario(FECHA_INVENTARIO,CANT_PRODUCTO_INVENTARIO,VALOR_ESTIMADO,DESCRIPCION_INVENTARIO,DEPARTAMENTO_ID_DEPARTAMENTO,PRODUCTO_ID_PRODUCTO)
        if salida == 1:
            return Response({'response':'Se creo correctamente el inventario'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_inventario(request,id):
    if request.method == 'GET':
        get_inventario = buscar_inventario(id)
        if(get_inventario != []):
            inventarios = []
            res = {}
            for invent in get_inventario:
                res = {}
                res['ID_INVENTARIO'] = invent[0]
                res['FECHA_INVENTARIO'] = invent[1]
                res['CANT_PRODUCTO_INVENTARIO'] = invent[2]
                res['VALOR_ESTIMADO'] = invent[3]
                res['DESCRIPCION_INVENTARIO'] = invent[4]
                res['DEPARTAMENTO_ID_DEPARTAMENTO'] = invent[5]
                res['PRODUCTO_ID_PRODUCTO'] = invent[6]
                inventarios.append(res)
            return Response(inventarios, status=status.HTTP_200_OK)
        elif(get_inventario == []):
            return Response({"Error": "No se encontraron inventarios"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def inventario_modify(request, id):
    if request.method == 'POST':
        get_inventario = buscar_inventario(id)
        if(get_inventario == []):
            return  Response({'response':'No existe un inventario'}, status=status.HTTP_404_NOT_FOUND)

        FECHA_INVENTARIO = request.data.get('FECHA_INVENTARIO')
        CANT_PRODUCTO_INVENTARIO = request.data.get('CANT_PRODUCTO_INVENTARIO')
        VALOR_ESTIMADO = request.data.get('VALOR_ESTIMADO')
        DESCRIPCION_INVENTARIO = request.data.get('DESCRIPCION_INVENTARIO')
        DEPARTAMENTO_ID_DEPARTAMENTO = request.data.get('DEPARTAMENTO_ID_DEPARTAMENTO')
        PRODUCTO_ID_PRODUCTO = request.data.get('PRODUCTO_ID_PRODUCTO')
        
        salida = modificar_inventario(id,FECHA_INVENTARIO,CANT_PRODUCTO_INVENTARIO,VALOR_ESTIMADO,DESCRIPCION_INVENTARIO,DEPARTAMENTO_ID_DEPARTAMENTO,PRODUCTO_ID_PRODUCTO)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el inventario'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def inventario_delete(request, id):
    if request.method == 'DELETE':
        get_inventario = eliminar_inventario(id)
        if(get_inventario == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe inventario con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_inventario(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente el inventario'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento CheckOut
@api_view(['GET', 'POST'])
def checkOut_list(request):
    if request.method == 'GET':
        get_checkOut = listar_checkOut()
        if(get_checkOut != []):
            checkOut = []
            res = {}
            for check in get_checkOut:
                res = {}
                res['ID_CHECK_OUT'] = check[0]
                res['FECHA_CHECK_OUT'] = check[1]
                res['OBSERVACION'] = check[2]
                res['RESERVA_ID_RESERVA'] = check[3]
                res['MULTA_ID_MULTA'] = check[4]
                checkOut.append(res)
            return Response(checkOut, status=status.HTTP_200_OK)
        elif(get_checkOut == []):
            return Response({"Error": "No se encontraron check-out"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def checkOut_create(request):
    if request.method == 'POST':
        FECHA_CHECK_OUT = request.data.get('FECHA_CHECK_OUT')
        OBSERVACION = request.data.get('OBSERVACION')
        RESERVA_ID_RESERVA = request.data.get('RESERVA_ID_RESERVA')
        MULTA_ID_MULTA = request.data.get('MULTA_ID_MULTA')
        
        salida = crear_checkOut(FECHA_CHECK_OUT,OBSERVACION,RESERVA_ID_RESERVA,MULTA_ID_MULTA)
        if salida == 1:
            return Response({'response':'Se creo correctamente el check-Out'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_checkOut(request,id):
    if request.method == 'GET':
        get_checkOut = buscar_checkOut(id)
        if(get_checkOut != []):
            checkOut = []
            res = {}
            for check in get_checkOut:
                res = {}
                res['ID_CHECK_IN'] = check[0]
                res['FECHA_CHECK_IN'] = check[1]
                res['OBSERVACION'] = check[2]
                res['RESERVA_ID_RESERVA'] = check[3]
                res['MULTA_ID_MULTA'] = check[4]
                checkOut.append(res)
            return Response(checkOut, status=status.HTTP_200_OK)
        elif(get_checkOut == []):
            return Response({"Error": "No se encontraron check-Out"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def checkOut_modify(request, id):
    if request.method == 'POST':
        get_checkOut = buscar_checkOut(id)
        if(get_checkOut == []):
            return  Response({'response':'No existe un Check-Out'}, status=status.HTTP_404_NOT_FOUND)

        FECHA_CHECK_IN = request.data.get('FECHA_CHECK_IN')
        OBSERVACION = request.data.get('OBSERVACION')
        RESERVA_ID_RESERVA = request.data.get('RESERVA_ID_RESERVA')
        MULTA_ID_MULTA = request.data.get('MULTA_ID_MULTA')
        
        salida = modificar_checkOut(id,FECHA_CHECK_IN,OBSERVACION,RESERVA_ID_RESERVA,MULTA_ID_MULTA)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el Check-Out'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def checkOut_delete(request, id):
    if request.method == 'DELETE':
        get_checkOut = eliminar_checkOut(id)
        if(get_checkOut == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe check-Out con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_checkOut(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente el check-Out'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento Servicio Extra
@api_view(['GET', 'POST'])
def servExtra_list(request):
    if request.method == 'GET':
        get_servicioExtra = listar_servicioExtra()
        if(get_servicioExtra != []):
            servExtra = []
            res = {}
            for servEx in get_servicioExtra:
                res = {}
                res['ID_SERVICIO'] = servEx[0]
                res['NOM_SERVICIO_EXTRA'] = servEx[1]
                res['VALOR_SERVICIO_EXTRA'] = servEx[2]
                servExtra.append(res)
            return Response(servExtra, status=status.HTTP_200_OK)
        elif(get_servicioExtra == []):
            return Response({"Error": "No se encontraron servicios extras"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def servExtra_create(request):
    if request.method == 'POST':
        NOM_SERVICIO_EXTRA = request.data.get('NOM_SERVICIO_EXTRA')
        VALOR_SERVICIO_EXTRA = request.data.get('VALOR_SERVICIO_EXTRA')
        
        salida = crear_servicioExtra(NOM_SERVICIO_EXTRA,VALOR_SERVICIO_EXTRA)
        if salida == 1:
            return Response({'response':'Se creo correctamente el servicio extra'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_servExtra(request,id):
    if request.method == 'GET':
        get_servicioExtra = buscar_servicioExtra(id)
        if(get_servicioExtra != []):
            servExtra = []
            res = {}
            for servEx in get_servicioExtra:
                res = {}
                res['ID_SERVICIO'] = servEx[0]
                res['NOM_SERVICIO_EXTRA'] = servEx[1]
                res['VALOR_SERVICIO_EXTRA'] = servEx[2]
                servExtra.append(res)
            return Response(servExtra, status=status.HTTP_200_OK)
        elif(get_servicioExtra == []):
            return Response({"Error": "No se encontraron servicios extras"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def servExtra_modify(request, id):
    if request.method == 'POST':
        get_servicioExtra = buscar_servicioExtra(id)
        if(get_servicioExtra == []):
            return  Response({'response':'No existe un servicios extras'}, status=status.HTTP_404_NOT_FOUND)

        NOM_SERVICIO_EXTRA = request.data.get('NOM_SERVICIO_EXTRA')
        VALOR_SERVICIO_EXTRA = request.data.get('VALOR_SERVICIO_EXTRA')
        
        salida = modificar_servicioExtra(id,NOM_SERVICIO_EXTRA,VALOR_SERVICIO_EXTRA)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el servicio extra'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def servExtra_delete(request, id):
    if request.method == 'DELETE':
        get_servicioExtra = eliminar_servicioExtra(id)
        if(get_servicioExtra == []):
            ##Revisar que cuando no se encuentre id deberia enviar mensaje de error.
            return  Response({'response':'No existe servicio extra con ese ID'}, status=status.HTTP_404_NOT_FOUND)
        else:
            salida = eliminar_servicioExtra(id)
    if salida == 1:
        return Response({'response':'Se eliminó correctamente el servicio extra'}, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Mantenimiento Pago

@api_view(['GET', 'POST'])
def pagoID_list(request):
    if request.method == 'GET':
        get_pagoID = listar_pagoID()
        if(get_pagoID != []):
            pagoID = []
            res = {}
            for pag_id in get_pagoID:
                res = {}
                res['ID_PAGO'] = pag_id[0]
                pagoID.append(res)
            return Response(pagoID, status=status.HTTP_200_OK)
        elif(get_pagoID == []):
            return Response({"Error": "No se encontraron servicios extras"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def pago_create(request):
    if request.method == 'POST':
        FECHA_PAGO = request.data.get('FECHA_PAGO')
        MONTO_TOTAL = request.data.get('MONTO_TOTAL')
        TIPO_PAGO_ID_TIPO_PAGO = request.data.get('TIPO_PAGO_ID_TIPO_PAGO')
        CORREO_USUARIO = request.data.get('CORREO_USUARIO')
        
        resp = envio_correo('Se genero un pago', 'su pago fue recepcionado con exito', CORREO_USUARIO)
        
        salida = crear_pago(FECHA_PAGO,MONTO_TOTAL,TIPO_PAGO_ID_TIPO_PAGO)
        if salida == 1:
            return Response({'response':'Se creo correctamente el pago'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#Mantenimiento Orden de compra

@api_view(['GET', 'POST'])
def OrdenCompra_list(request):
    if request.method == 'GET':
        get_OrdenCompra = listar_OrdenCompra()
        if(get_OrdenCompra != []):
            ordenCompra = []
            res = {}
            for ordenCom in get_OrdenCompra:
                res = {}
                res['ID_ORDEN_COMPRA'] = ordenCom[0]
                res['FECHA_ORDEN_COMPRA'] = ordenCom[1]
                res['DEBE'] = ordenCom[2]
                res['TOTAL_COMPRA'] = ordenCom[3]
                res['RESERVA_ID_RESERVA'] = ordenCom[4]
                res['PAGO_ID_PAGO'] = ordenCom[5]
                ordenCompra.append(res)
            return Response(ordenCompra, status=status.HTTP_200_OK)
        elif(get_OrdenCompra == []):
            return Response({"Error": "No se encontraron ordenes de compras"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def OrdenCompra_create(request):
    if request.method == 'POST':
        FECHA_ORDEN_COMPRA = request.data.get('FECHA_ORDEN_COMPRA')
        DEBE = request.data.get('DEBE')
        TOTAL_COMPRA = request.data.get('TOTAL_COMPRA')
        RESERVA_ID_RESERVA = request.data.get('RESERVA_ID_RESERVA')
        PAGO_ID_PAGO = request.data.get('PAGO_ID_PAGO')
        
        salida = crear_ordenCompra(FECHA_ORDEN_COMPRA,DEBE,TOTAL_COMPRA,RESERVA_ID_RESERVA,PAGO_ID_PAGO)
        if salida == 1:
            return Response({'response':'Se creo correctamente la orden de compra'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def OrdenCompra_modify(request, id):
    if request.method == 'POST':
        get_ordenCompra = buscar_ordenCompra(id)
        if(get_ordenCompra == []):
            return  Response({'response':'No existe una orden de compra'}, status=status.HTTP_404_NOT_FOUND)

        FECHA_ORDEN_COMPRA = request.data.get('FECHA_ORDEN_COMPRA')
        DEBE = request.data.get('DEBE')
        TOTAL_COMPRA = request.data.get('TOTAL_COMPRA')
        RESERVA_ID_RESERVA = request.data.get('RESERVA_ID_RESERVA')
        PAGO_ID_PAGO = request.data.get('PAGO_ID_PAGO')
        
        salida = modificar_ordenCompra(id,FECHA_ORDEN_COMPRA,DEBE,TOTAL_COMPRA,RESERVA_ID_RESERVA,PAGO_ID_PAGO)
        if salida == 1:
            return Response({'response':'Se modifico correctamente el servicio extra'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_OrdenCompra(request,id):
    if request.method == 'GET':
        get_OrdenCompra = buscar_ordenCompra(id)
        if(get_OrdenCompra != []):
            ordenCompra = []
            res = {}
            for ordenCom in get_OrdenCompra:
                res = {}
                res['ID_ORDEN_COMPRA'] = ordenCom[0]
                res['FECHA_ORDEN_COMPRA'] = ordenCom[1]
                res['DEBE'] = ordenCom[2]
                res['TOTAL_COMPRA'] = ordenCom[3]
                res['RESERVA_ID_RESERVA'] = ordenCom[4]
                res['PAGO_ID_PAGO'] = ordenCom[5]
                ordenCompra.append(res)
            return Response(ordenCompra, status=status.HTTP_200_OK)
        elif(get_OrdenCompra == []):
            return Response({"Error": "No se encontraron orden de compras"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_OrdenCompraReserva(request,id):
    if request.method == 'GET':
        get_OrdenCompra = buscar_ordenReserva(id)
        if(get_OrdenCompra != []):
            ordenCompra = []
            res = {}
            for ordenCom in get_OrdenCompra:
                res = {}
                res['ID_ORDEN_COMPRA'] = ordenCom[0]
                res['FECHA_INGRESO'] = ordenCom[1]
                res['FECHA_SALIDA'] = ordenCom[2]
                res['CANT_DIA_RESERVA'] = ordenCom[3]
                res['ESTADO_RESERVA'] = ordenCom[4]
                res['DEBE'] = ordenCom[5]
                res['TOTAL_COMPRA'] = ordenCom[6]
                res['RESERVA_ID_RESERVA'] = ordenCom[7]
                ordenCompra.append(res)
            return Response(ordenCompra, status=status.HTTP_200_OK)
        elif(get_OrdenCompra == []):
            return Response({"Error": "No se encontraron orden de compras"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#TransBank
@api_view(['POST'])
def create_transaction(request):
    if request.method == 'POST':
        buy_order = request.data.get('buy_order')
        session_id = request.data.get('session_id')
        amount = request.data.get('amount')
        return_url = request.data.get('return_url')

        body = {"buy_order": buy_order, "session_id": session_id, "amount": amount, "return_url": return_url}
        resp = crearTransaction(json.dumps(body))
        request.session['tbk_token'] = resp['token']
    
        return Response( resp, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def commit_transaction(request):
    if request.method == 'POST':
        token = request.data.get('token_ws')
        resp = transactionCommit(token)
        return Response( resp, status=status.HTTP_200_OK)
    else:
        return Response({'response':'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def envio_correo(subject, message, mailto ):
    resp =  send_mail(
        subject,
        message,
        'turismorealscrumbot@gmail.com',
        [mailto],
        fail_silently=False,
    );

    return resp;




