"""
La suma de los cuadrados de los primeros diez números naturales es,

El cuadrado de la suma de los primeros diez números naturales es,

Por lo tanto, la diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es .

Calcula la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.
"""

n=101
def numeroCuadrado(n):
    for x in range(n):
        c=x**2
        yield c
def numeros(n):
    for x in range(n):
        yield x

sumaCuadrados=sum(numeroCuadrado(n))
sumaNumeros=sum(numeros(n))
cuadradosSumaNumeros=sumaNumeros**2
resta=cuadradosSumaNumeros-sumaCuadrados
print("La resta es: "+str(resta))



