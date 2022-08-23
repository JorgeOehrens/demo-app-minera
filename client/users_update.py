from client.models import Entrada , Item , Asignacion, Salida, Registro_stock
from django.db.models import Sum




item_table=Item.objects.all() #Todos los item 





list_sum=[]
list_rest=[]
sum_entrada=0
sum_salida=0

for i in item_table:

    registro_stock_table=Registro_stock.objects.filter(item=i.id).order_by('fecha')  #Todos los registros

    list_sum=[]
    list_rest=[]
    sum_entrada=0
    sum_salida=0


    for a in registro_stock_table:
        

        if a.movimiento == "Salida":

            cantidad=a.cantidad

            list_rest.append(cantidad)

            sum_salida= sum(list_rest)
            stock_total_registro= sum_entrada-sum_salida



        else:
            cantidad=a.cantidad

            list_sum.append(cantidad)

            sum_entrada=sum(list_sum)

            stock_total_registro= sum_entrada-sum_salida




        


        actualizar_stock=Item.objects.get(nombre=a.item)

        actualizar_stock.total_item=stock_total_registro
        actualizar_stock.save()

        act_stock_registro=Registro_stock.objects.get(id=a.id)
        act_stock_registro.stock=stock_total_registro
        act_stock_registro.save()

        

        





