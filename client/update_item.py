from client.models import Entrada , Item , Asignacion, Salida, Registro_stock
from django.db.models import Sum




item_table=Item.objects.all() #Todos los item 


for i in item_table:

    registro_stock_table=Registro_stock.objects.filter(item=i.id).order_by('fecha')  #Todos los registros
    registro_stock_table_s=Registro_stock.objects.filter(item=i.id).order_by('-fecha')  #Todos los registros

    

    registro_stock_table_item =registro_stock_table_s.filter(item=i.id)[:2]

    
    if registro_stock_table_item:
        nuevo_registro=registro_stock_table_item[0]
        ultimo_registro=registro_stock_table_item[1]

        nuevo_registro_cantidad=nuevo_registro.cantidad

        # print(nuevo_registro.movimiento)
        # print(nuevo_registro.cantidad)
        # print(nuevo_registro.stock)
        # print("2")

        # print(ultimo_registro.movimiento)
        # print(ultimo_registro.cantidad)
        # print(ultimo_registro.stock)
        # print("---------------")

        ultimo_registro_stock=ultimo_registro.stock


        if nuevo_registro.movimiento == "Salida":

            stock_reminente=ultimo_registro_stock - nuevo_registro_cantidad

            # print(stock_reminente)

            actualizar_stock=Item.objects.get(nombre=i.nombre)
            actualizar_stock.total_item=stock_reminente
            actualizar_stock.save()

            act_stock_registro=Registro_stock.objects.get(id=nuevo_registro.id)
            act_stock_registro.stock=stock_reminente
            act_stock_registro.save()
        else:
            stock_reminente=ultimo_registro_stock + nuevo_registro_cantidad
            # print(stock_reminente)

            actualizar_stock=Item.objects.get(nombre=i.nombre)
            actualizar_stock.total_item=stock_reminente
            actualizar_stock.save()

            act_stock_registro=Registro_stock.objects.get(id=nuevo_registro.id)
            act_stock_registro.stock=stock_reminente
            act_stock_registro.save()
    



        



 




        

        

        



