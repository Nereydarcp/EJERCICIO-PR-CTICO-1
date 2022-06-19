"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products 


Nombre_usuario = "Emtech"
Contraseña = "Caso1"
access = False 
while True:
  Solicitar_usuario = input("Ingresa el usuario: ")
  Solicitar_contraseña = input("Ingrese la contraseña: ")
  if Solicitar_usuario in Nombre_usuario and Solicitar_contraseña in Contraseña:
    if Solicitar_usuario.index(Nombre_usuario) == Contraseña.index(Solicitar_contraseña):
      access = True
      break
    else:
      print("Vuelve a intentarlo: ")
  else:
   print("Vuelve a intentarlo: ")
if access:
  pass
  print("Reporte de productos: ")


contador = 0
total_ventas_productos = []
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador += 1
  formato_ideal = [producto[0], contador]
  total_ventas_productos.append(formato_ideal)
  contador = 0

  #ordenar productos por mayor cantidad de ventas 
  productos_más_vendidos = []
while total_ventas_productos:
  maximo = total_ventas_productos[0][1]
  lista_actual = total_ventas_productos[0]
  for venta_producto in total_ventas_productos:
    if venta_producto[1] > maximo:
      maximo = venta_producto[1]
      lista_actual = venta_producto
      
  productos_más_vendidos.append(lista_actual)
  total_ventas_productos.remove(lista_actual)

print(total_ventas_productos[0:5])
print(f'Estos son los cinco productos con mayores ventas: ', productos_más_vendidos[0:5])


contador = 0
total_búsquedas_productos = []
for producto in lifestore_products:
  for búsqueda in lifestore_searches:
    if producto[0] == búsqueda[1]:
      contador += 1
  formato_ideal = [producto[0], contador]
  total_búsquedas_productos.append(formato_ideal)
  contador = 0

  #Ordenar productos con mayores búsquedas
  productos_más_búscados = []
while total_búsquedas_productos:
  maximo = total_búsquedas_productos[0][1]
  lista_actual = total_búsquedas_productos[0]
  for búsqueda_producto in total_búsquedas_productos:
    if búsqueda_producto[1] > maximo:
      maximo = búsqueda_producto[1]
      lista_actual = búsqueda_producto
      
  productos_más_búscados.append(lista_actual)
  total_búsquedas_productos.remove(lista_actual)

print(total_búsquedas_productos[0:10])
print(f'Estos son los diez productos con mayores búsquedas: ', productos_más_búscados[0:10])

contador = 0
total_ventas_productos = []
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador += 1
  formato_ideal = [producto[0], contador]
  total_ventas_productos.append(formato_ideal)
  contador = 0

  #ordenar productos por menor cantidad de ventas 
  productos_menos_vendidos = []
while total_ventas_productos:
  minimo = total_ventas_productos[0][1]
  lista_actual = total_ventas_productos[0]
  for venta_producto in total_ventas_productos:
    if venta_producto[1] < minimo:
      minimo = venta_producto[1]
      lista_actual = venta_producto
      
  productos_menos_vendidos.append(lista_actual)
  total_ventas_productos.remove(lista_actual)

print(total_ventas_productos[0:5])
print(f'Estos son los cinco productos con menores ventas: ', productos_menos_vendidos[0:5])


contador = 0
total_búsquedas_productos = []
for producto in lifestore_products:
  for búsqueda in lifestore_searches:
    if producto[0] == búsqueda[1]:
      contador += 1
  formato_ideal = [producto[0], contador]
  total_búsquedas_productos.append(formato_ideal)
  contador = 0

  #Ordenar productos con menores búsquedas
  productos_menos_búscados = []
while total_búsquedas_productos:
  minimo = total_búsquedas_productos[0][1]
  lista_actual = total_búsquedas_productos[0]
  for búsqueda_producto in total_búsquedas_productos:
    if búsqueda_producto[1] < minimo:
      minimo = búsqueda_producto[1]
      lista_actual = búsqueda_producto
      
  productos_menos_búscados.append(lista_actual)
  total_búsquedas_productos.remove(lista_actual)

print(total_búsquedas_productos[0:10])
print(f'Estos son los diez productos con menores búsquedas: ', productos_menos_búscados[0:10])

