"""
2 15 = 32768 y la suma de sus dígitos es 3 + 2 + 7 + 6 + 8 = 26.

¿Cuál es la suma de los dígitos del número 2 1000 ?

"""

potencia=1

for i in range(1000):
    potencia=potencia*2
 
texto=(str(potencia))

suma=0
for i in texto:
    valor=int(i)
    suma= suma+valor

print("La suma de los digitos de la potencia de 2 elevado a la 1000 es: " + str(suma) + " y el valor de la potencia es: " + str(potencia))