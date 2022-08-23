from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import  messages
import datetime
from .models import Entrada , Item , Asignacion, Salida, Registro_stock, Frente
from .forms import PostForm
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='login')

def home(request):

    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email
    
    context= {
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'usuario':usuario
    

    }
        


    if request.method == "GET":
        return render ( request , 'Client/Home/index.html',context)


@login_required(login_url='login')
def frentes_registro(request):
    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email
    frentes=Frente.objects.order_by('nombre')
    
    context= {
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'usuario':usuario,
        'frentes':frentes
    

    }
        


    if request.method == "GET":
        return render ( request , 'Client/Frentes/create.html',context)
    
    if request.method == "POST":
        nombre=request.POST['nombre']
        
        Frente.objects.create(nombre=nombre)
        
        return render ( request , 'Client/Frentes/create.html',context)





@login_required(login_url='login')
def avance(request):

    usuario=User.objects.get(username=request.user)
    first_name=usuario.first_name
    last_name=usuario.last_name
    email=usuario.email
    
    
        

    registro_stock=Registro_stock.objects.all().order_by('-fecha')
    fecha=datetime.datetime.now()
    hora=datetime.datetime.now().strftime('%H:%M:%S')

    a= fecha -datetime.timedelta(days=3)

    año_a=str(a.year)
    mes_a='0'+str(a.month)
    dia_a=str(a.day)


    stock_pretroleo=Item.objects.get(nombre='Petróleo')

    frente = Frente.objects.order_by('nombre')

    stock_pretroleo=stock_pretroleo.total_item



   
    dia=str(fecha.day)
    mes='0'+str(fecha.month)
    año=str(fecha.year)
    context= {
        'Entradas':registro_stock,
        'Item':Item.objects.order_by('nombre'),
        'dia':dia,
        'mes':mes,
        'año':año,
        'hora':hora,
        'dia_a':dia_a,
        'mes_a':mes_a,
        'año_a':año_a,

        'Asignaciones':Asignacion.objects.order_by('nombre'),
        'stock_pretroleo':stock_pretroleo,
        'frente':frente,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'usuario':usuario

    }
    if request.method == 'POST':
        fecha=datetime.datetime.now()
        item='d'
        movimiento='Ingreso'
        cantidad=request.POST['cantidad']
        horometro=request.POST['horometro']



        stock=0


        
        item=Item.objects.get(nombre=item)



        

        Entrada.objects.create(creador_registro=request.user, fecha_registro=fecha,
        item=item , movimiento=movimiento,cantidad=cantidad,horometro=horometro ,stock=stock)

        





        datos = {}



        

        datos['resultado']="Entrada Creado exitosamente"

        exec(open('client/update_item.py').read())

        
        return HttpResponse('')

    return render ( request , 'Client/Avance/index.html' , context)


@login_required(login_url='login')
def Salida2(request):
    exec(open('client/users_update.py').read())

    salida=Salida.objects.filter(creador_registro=request.user).order_by('-fecha_registro')
    context= {
        'Salidas':salida,
        'Item':Item.objects.all(),
    }
    if request.method == 'POST':
        fecha=datetime.datetime.now()
        item='d'
        movimiento='Ingreso'
        cantidad=request.POST['cantidad']
        horometro=request.POST['horometro']



        stock=0


        
        item=Item.objects.get(nombre=item)



        

        Salida.objects.create(creador_registro=request.user, fecha_registro=fecha,
        item=item , movimiento=movimiento,cantidad=cantidad,horometro=horometro ,stock=stock)

        





        datos = {}



        

        datos['resultado']="Salida Creado exitosamente"
        
        
        return HttpResponse('')

    return render ( request , 'Client/Salida/index.html' , context)



@login_required(login_url='login')
def CrearSalida(request):


    if request.method == 'POST':
        fecha=datetime.datetime.now()
        item=request.POST['item']

        asignacion=request.POST['asignacion']

        # item='Petróleo'
        movimiento='Salida'
        cantidad=request.POST['cantidad']
        fecha_salida=request.POST['fecha_salida']
        item=Item.objects.get(nombre=item)
        


        if item.nombre == "Petróleo":
            horometro=request.POST['horometro']
            frente=Frente.objects.get(nombre='x')



            asignacion=Asignacion.objects.get(nombre=asignacion)

            
            if 'imagen_horometro' in request.FILES:
                imagen_horometro = request.FILES['imagen_horometro']
            else:
                imagen_horometro=0
                


            ultimo_registro=Registro_stock.objects.filter(item=item).order_by('-fecha')[:1]
            if not ultimo_registro:
                stock_remanente=0
            else:
                for a in ultimo_registro:
                    stock_remanente=a.stock
                    break

            stock_final= stock_remanente - int(cantidad)

            item_obj=Item.objects.get(nombre=item)

            item_obj.total_item=stock_final
            item_obj.save()

            if imagen_horometro == 0:
                Salida.objects.create(creador_registro=request.user, fecha_registro=fecha,
                    item=item ,movimiento=movimiento,cantidad=cantidad,horometro=horometro,fecha_salida=fecha_salida, asignacion=asignacion ,frente=frente)

                Registro_stock.objects.create(creador_registro=request.user, fecha_registro=fecha,item=item ,movimiento=movimiento,cantidad=cantidad,horometro=horometro,fecha=fecha_salida, asignacion=asignacion ,frente=frente,stock=stock_final, imagen=0)

            else:






                Salida.objects.create(creador_registro=request.user, fecha_registro=fecha,
                    item=item ,movimiento=movimiento,cantidad=cantidad,horometro=horometro,fecha_salida=fecha_salida, asignacion=asignacion ,frente=frente)

                Registro_stock.objects.create(creador_registro=request.user, fecha_registro=fecha,item=item ,movimiento=movimiento,cantidad=cantidad,horometro=horometro,fecha=fecha_salida, asignacion=asignacion ,frente=frente,stock=stock_final, horometro_imagen2=imagen_horometro,imagen=1)

            return redirect(avance)

        


        else:
            asignacion=Asignacion.objects.get(nombre='x')
            
            frente=request.POST['frente']
            frente=Frente.objects.get(nombre=frente)


            ultimo_registro=Registro_stock.objects.filter(item=item).order_by('-fecha')[:1]
            if not ultimo_registro:
                stock_remanente=0
            else:
                for a in ultimo_registro:
                    stock_remanente=a.stock
                    break

            stock_final= stock_remanente - int(cantidad)

            item_obj=Item.objects.get(nombre=item)

            item_obj.total_item=stock_final
            item_obj.save()




            Salida.objects.create(creador_registro=request.user, fecha_registro=fecha,
                item=item ,movimiento=movimiento,cantidad=cantidad,fecha_salida=fecha_salida, asignacion=asignacion , frente=frente)

            Registro_stock.objects.create(creador_registro=request.user, fecha_registro=fecha,
                item=item ,movimiento=movimiento,cantidad=cantidad,fecha=fecha_salida, asignacion=asignacion,frente=frente,stock=stock_final )


            return redirect(avance)




        

        



        







        

        
        
        


        

@login_required(login_url='login')
def CrearPost(request):


    if request.method == 'POST':
        fecha=datetime.datetime.now()
        item=request.POST['item']

        # item='Petróleo'
        movimiento='Ingreso'
        cantidad=request.POST['cantidad']
        # asignacion='Compresor Atlas'
        fecha_ingreso=request.POST['fecha_ingreso']
        
        item=Item.objects.get(nombre=item)

        asignacion=Asignacion.objects.get(nombre='x')

        frente=Frente.objects.get(nombre='x')

        ultimo_registro=Registro_stock.objects.filter(item=item).order_by('-fecha')[:1]
        if not ultimo_registro:
            stock_remanente=0
        else:
            for a in ultimo_registro:
                stock_remanente=a.stock
                break

        stock_final= stock_remanente + int(cantidad)

        item_obj=Item.objects.get(nombre=item)

        item_obj.total_item=stock_final
        item_obj.save()


        Registro_stock.objects.create(creador_registro=request.user, fecha_registro=fecha,
        item=item ,movimiento=movimiento,cantidad=cantidad,fecha=fecha_ingreso, asignacion=asignacion,frente=frente,stock=stock_final )

        

        Entrada.objects.create(creador_registro=request.user, fecha_registro=fecha,
        item=item ,movimiento=movimiento,cantidad=cantidad,fecha_entrada=fecha_ingreso )







        









    

        







        

        
        
        return redirect(avance)


