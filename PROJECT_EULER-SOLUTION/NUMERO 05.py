"""
2520 es el número más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin ningún resto.

¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?

"""

"""
NOTA SOBRE EL PROBLEMA
el primer intento esta comentado pero lo dejo aunque demora mucho dado que es interesante el metodo importado itertools que hace que un rango pueda ser infinito cuando desconocemos el tope del mismo

"""

# import itertools

# listaRango=[3,4,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
# def localiza():
#     contador=0
#     for i in itertools.count(20):
#         print(i)
#         for j in listaRango:
#             if i % j== 0:
#                 contador += 1                       
#                 if j==20 and contador == 16:
#                     #print(i)                    
#                     #print(j)
#                     return i
#             else:
#                 contador=0
#print("El valor que es multiplo desde el 1 al 20 inclusive es: " + str(localiza()))

i=20

while i % 1 != 0 or i % 2 != 0 or i % 3 != 0 or i % 4 != 0 or i % 5 != 0 or i % 6 != 0 or i % 7 != 0 or i % 8 != 0 or i % 9 != 0 or i % 10 != 0 or  i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0 :
    i+=20
    
print("El valor que es multiplo desde el 1 al 20 inclusive es: " + str(i))