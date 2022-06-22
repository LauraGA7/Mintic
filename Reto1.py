
print ('Bienvenidos a "Los vecinos"')
codigo_producto = int(input())
nombre_producto = str(input())
cantidad = float(input())
precio = float(input())
noIVA=(cantidad * precio)
IVA = (noIVA*0.19)+noIVA
print (codigo_producto)
print(nombre_producto)
print(noIVA)
print(IVA)