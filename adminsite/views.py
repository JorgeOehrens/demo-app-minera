from django.shortcuts import render, redirect
from datetime import datetime
from client.models import Entrada, Salida , Registro_stock, Item, Asignacion, Frente
import django_excel as excel
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.contrib import  messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,  DjangoUnicodeDecodeError
import datetime
from django.contrib.admin.views.decorators import staff_member_required
import pandas as pd
import numpy as np
from django.db.models import Sum

# Create your views here.



@staff_member_required

def home(request):
    registros = Registro_stock.objects.all().order_by('-fecha')
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email
    items=Item.objects.all()


        



    empleados = User.objects.all()

    empleados_no_staff=empleados.filter(is_staff=False)

    n_empleados_no_staff=empleados_no_staff.count()







    registros_ingresos=registros.filter(movimiento="Ingreso")
    registros_salidas=registros.filter(movimiento="Salida")

    fecha_actual=datetime.datetime.now()
    fecha= fecha_actual +datetime.timedelta(days=1)    

    # fecha=fecha +datetime.timedelta(days=)    

    año=str(fecha.year)
    mes=str(fecha.month)
    dia=str(fecha.day)


    a= fecha_actual -datetime.timedelta(days=8)    
    año_a=str(a.year)
    mes_a=str(a.month)
    dia_a=str(a.day)
    fecha_semana=año_a + "-" + mes_a + "-" + dia_a
    fecha_hoy=año + "-" + mes + "-" + dia

    items_stock=items.exclude(total_item=0)

    n_items_stock=items_stock.count()

    n_items=items.count()

    



    



    registros_total=registros[:5]



    regsitros_ingresos_fecha=registros_ingresos.filter(fecha__range=[fecha_semana, fecha_hoy]) 
    n_regsitros_ingresos_fecha=regsitros_ingresos_fecha.count()

    registros_salidas_fecha=registros_salidas.filter(fecha__range=[fecha_semana, fecha_hoy]) 
    n_registros_salidas_fecha=registros_salidas_fecha.count()




    context= { 
        'registros':registros,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'n_empleados_no_staff':n_empleados_no_staff,
        'n_regsitros_ingresos_fecha':n_regsitros_ingresos_fecha,
        'n_registros_salidas_fecha':n_registros_salidas_fecha,
        'n_items_stock':n_items_stock,
        'n_items':n_items,
        'items':items_stock,
        'registros_total':registros_total,
        'items_todos':items_stock
        
    }

    if request.method == "GET":
        return render ( request , 'Admin/Home/index.html',context )




@staff_member_required

def registro_fecha(request,id):
    items=Item.objects.all()
    items_stock=items.exclude(total_item=0)
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email

    registros=Registro_stock.objects.filter(item=id).order_by('-fecha')
    registros_ingresos=registros.filter(movimiento="Ingreso")
    registros_salidas=registros.filter(movimiento="Salida")

    item=Item.objects.get(id=id)

    registros_fechas=registros.values_list('fecha',flat=True)
    lista=[]

    for title in registros_fechas:
        registros_fechas_array=title.strftime('%d-%m-%y')

        lista.append(registros_fechas_array)


    lista_unica=np.unique(lista)

    dias_activos=len(lista_unica) 
    sum_cantidad = list(registros.aggregate(Sum('cantidad')).values())[0]

    promedio_diario=round(sum_cantidad/dias_activos)



    print(promedio_diario)









    


    
    
    stock_remanente=item.total_item

    



        
    filtrado_count=registros.count()
    ingresos_count=registros_ingresos.count()
    salidas_count=registros_salidas.count()


    context= { 
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'stock_remanente':stock_remanente,
        'filtrado_count':filtrado_count,
        'ingresos_count':ingresos_count,
        'salidas_count':salidas_count,
        'item':item,
        'registros':registros,
        'items_todos':items_stock
        
    }

    if request.method == "GET":
        
        return render ( request , 'Admin/Stock/item.html',context )
    
    if request.method=="POST":
        fecha_inicio = request.POST['fecha_inicio']
        fecha_termino = request.POST['fecha_termino']
        registros = Registro_stock.objects.all().order_by('-fecha')



        registros=registros.filter(item=id)
        registros_filtrado=registros.filter(date__gte=fecha_inicio,date__lte=fecha_termino)
        registros_ingresos=registros_filtrado.filter(movimiento="Ingreso")
        registros_salidas=registros_filtrado.filter(movimiento="Salida")
        
        registros_ingreso_ultimo=registros[:1]

        
        filtrado_count=registros_filtrado.count()
        ingresos_count=registros_ingresos.count()
        salidas_count=registros_salidas.count()

        
        return render ( request , 'Admin/Stock/item.html',context )

        

        






        
@staff_member_required

def usuarios(request):

    items=Item.objects.all()
    items_stock=items.exclude(total_item=0)
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email

    usuarios=User.objects.all()



    context= { 
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'items_todos':items_stock,
        'usuarios':usuarios
        
    }

    if request.method == "GET":
        return render ( request , 'Admin/Usuarios/index.html',context )




def eliminar_registro(request,id):

    registro_eliminar=Registro_stock.objects.filter(id=id)

    registro_eliminar.delete()

    return redirect(registros_total)



@staff_member_required

def edit_registro(request,id):
    items=Item.objects.all()
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email
    items=Item.objects.all()
    asignacioens= Asignacion.objects.all()

    frentes=Frente.objects.all()

    registro_edit=Registro_stock.objects.get(id=id)
    a=registro_edit.fecha
    hora=a.strftime('%H:%M:%S')

    id_regis=id

    dia_a=a.day
    mes_a=a.month


    if dia_a<10:
        dia_a='0'+str(a.day)
    else:
        dia_a=str(a.day)
    if mes_a<10:
        mes_a='0'+str(a.month)
    else:
        mes_a=str(a.month)




    
    año_a=str(a.year)
    print(año_a,mes_a,dia_a)

   


    context= { 
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'registro_edit':registro_edit,
        'items':items,
        'asignacioens':asignacioens,
        'frentes':frentes,
        'año_a':año_a,
        'mes_a':mes_a,
        'dia_a':dia_a,
        'hora':hora,
        'id_regis':id_regis

             
    }

    if request.method == "GET":
        return render ( request , 'Admin/Stock/registro_edit.html',context )


    if request.method == "POST":

        fecha=request.POST['fecha']

        item=request.POST['item']
        movimiento=request.POST['movimiento']
        cantidad=request.POST['cantidad']
        horonometro=request.POST['horometro']
        horonometro_imagen=request.FILES.get('imagen_horometro')
        asignacion=request.POST['asignacion']
        frente=request.POST['frente']

        # stock=


        # item='Petróleo'
        item=Item.objects.get(nombre=item)
        asignacion=Asignacion.objects.get(nombre=asignacion)
        frente=Frente.objects.get(nombre=frente)

        registro_edit.item=item
        registro_edit.movimiento=movimiento
        registro_edit.cantidad=cantidad
        # regsitro_edit.stock=stock
        registro_edit.horometro_imagen=horonometro_imagen
        registro_edit.asignacion=asignacion
        registro_edit.frente=frente
        registro_edit.fecha=fecha
        registro_edit.save()


    
        return render ( request , 'Admin/Stock/registro_edit.html',context )



@staff_member_required

def usuarios_details(request,id):

    items=Item.objects.all()
    items_stock=items.exclude(total_item=0)
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email

    usuario_detalles=User.objects.filter(id=id)

    registros_usuario=Registro_stock.objects.filter(creador_registro=id)

    registros_ingreso=registros_usuario.filter(movimiento='Ingreso')
    registros_salida=registros_usuario.filter(movimiento='Salida')

    count_regist=registros_usuario.count()
    count_ingreso=registros_ingreso.count()
    count_salida=registros_salida.count()




    context= { 
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'items_todos':items_stock,
        'usuario_detalles':usuario_detalles,
        'count_regist':count_regist,
        'count_ingreso':count_ingreso,
        'count_salida':count_salida,
        'registros_usuario':registros_usuario
        
    }

    if request.method == "GET":
        return render ( request , 'Admin/Usuarios/details.html',context )








@staff_member_required

def registros_total(request):

    items=Item.objects.all()
    items_stock=items.exclude(total_item=0)
    registros = Registro_stock.objects.all().order_by('-fecha')
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email


    context= { 
        'registros':registros,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'items_todos':items_stock
        
    }

    if request.method == "GET":
        return render ( request , 'Admin/Stock/index2.html',context )

@staff_member_required

def control_stock(request):
    registros = Registro_stock.objects.all().order_by('-fecha')
    items=Item.objects.all()
    items_stock=items.exclude(total_item=0)
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email
    item = Item.objects.all().order_by('-nombre')


    context= { 
        'registros':registros,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'item':item,
        'items_todos':items_stock
        
    }

    if request.method == "GET":
        return render ( request , 'Admin/Stock/index.html',context )



@staff_member_required


def actualizar_stock(request):
    exec(open('client/users_update.py').read())

    return redirect(control_stock )

@staff_member_required

def listresults(request):
    export = []
    # Se agregan los encabezados de las columnas
    export.append([
        'Ordenar por fecha',
        'Item',
        'Unidad',
        'Movimiento',
        'Cantidad',
        'Stock remanente',
        'Asignación',
        'Frente',
        'Horómetro',
        'Registrado por',
        'Fecha registro'])

    # Se obtienen los datos de la tabla o model y se agregan al array
    results = Registro_stock.objects.all().order_by('-fecha')
    for result in results:
        # ejemplo para dar formato a fechas, estados (si/no, ok/fail) o
        # acceder a campos con relaciones y no solo al id


        first_name= result.creador_registro.first_name
        last_name= result.creador_registro.last_name

        full_name = first_name + ' ' + last_name

        if result.asignacion.nombre == "x":
            asignacion=" "
        else:
            asignacion=result.asignacion.nombre

        
        if result.frente.nombre == "x":
            frente=" "
        else:
            frente=result.frente.nombre
 


        export.append([
                "{0:%Y-%m-%d %H:%M}".format(result.fecha),
                result.item.nombre,
                result.item.unidad,
                result.movimiento,
                result.cantidad,
                result.stock,
                asignacion,
                frente,
                result.horometro,
                full_name,

                "{0:%Y-%m-%d %H:%M}".format(result.fecha_registro),

                ])

    # Obtenemos la fecha para agregarla al nombre del archivo

    today    = datetime.datetime.now()
    strToday = today.strftime("%Y%m%d")

    # se transforma el array a una hoja de calculo en memoria
    sheet = excel.pe.Sheet(export)

    # se devuelve como "Response" el archivo para que se pueda "guardar"
    # en el navegador, es decir como hacer un "Download"
    return excel.make_response(sheet, "xlsx", file_name="RegistroStock-"+strToday+".xlsx")




def registro(request):

    if request.method =='GET':
        return render(request,'Registro/index.html')


    if request.method =='POST':
        #GET USER DATA
        #VALIDATE
        #CREATE USER CONT
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST ['email']
        password = 'xxxxxxxx'
        context = {
            'fieldValues': request.POST
        }


        if not User.objects.filter(username=username).exists():

            if not User.objects.filter(email=email).exists():

                if len(password)<8:
                    messages.warning(request,"Por favor complete todos los campos. Contraseña debe ser mayor a 8 caracteres.")
                    return render(request, 'Registro/index.cshtml', context)

                staff = request.POST.getlist('staff')


                if not staff:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name, )
                    user.set_password(password)
                    user.is_active=True
                    user.save()
                    correo= email


                    
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name, )
                    user.set_password(password)
                    user.is_active=True
                    user.is_staff=True
                    user.is_superuser=True
                    print(staff)

                    user.save()
                    correo= email


                    

                user = User.objects.filter(email=email)[0]
                user_username= user.username
                user_firstname=user.first_name
                user_lastname=user.last_name
                current_site= get_current_site(request)

                domain=current_site.domain



                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token=default_token_generator.make_token(user)

                print('http://', domain,' token= ', token,'uid= ',uid)


                subject_conf = 'GMS | Nuevo usuario'

                correo_admin= "jorge.oehrens@gmail.com"



                correo_html = render_to_string('partials/registro/email_inicial.html', {
                    'user': user,
                    'domain': domain,
                    'uid': uid,
                    "email":user.email,
                    'token': token,
                    'protocol': 'https',
                    'user_username': user.username,
                    'user_firstname':user.first_name,
                    'user_lastname': user.last_name,

                })

                text_content= strip_tags(correo_html)
                email = EmailMultiAlternatives(
                    subject_conf,text_content,
                                to=[correo])


                email.fail_silenty=False
                email.attach_alternative(correo_html,'text/html')
                email.send()















                

                messages.success(request,"Se realizado con exito la creacion del usuario")



                return render(request, 'Registro/index.html')




            else:
                messages.warning(request,"Usuario ya existe")
                # print(1)
                return render(request, 'Registro/index.html', context)



        messages.warning(request,"Usuario ya existe")
        # print(2)
        return render(request, 'Registro/index.html', context)




def confirmar_contraseña(request):
    
    if request.method == "GET":
        return render ( request , 'Registro/confirmar_contraseña.html')

    if request.method =="POST":
        return render ( request , 'Registro/confirmar_contraseña.html')


    


