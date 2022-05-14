"""
Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.
"""



print(sum([n for n in range (1000) if n % 5 == 0 or n % 3 == 0]))

suma=0
for n in range(1000):
    if  n % 5 == 0 or n % 3 == 0:
        suma=n+suma

print(suma)        
