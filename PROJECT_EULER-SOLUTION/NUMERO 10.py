"""
La suma de los números primos por debajo de 10 es 2 + 3 + 5 + 7 = 17.

Encuentra la suma de todos los números primos por debajo de dos millones.

"""


def esPrimo(num):
    if num == 0: return False
    if num <= 3: return True
    i = 2
    while i * i < num + 1:
        if num % i == 0: return False
        i += 1
    return True

def anexa():
    for n in range(2000000):        
        if esPrimo(n) and n != 1:
           yield n

sumaNumerosPrimos=sum(anexa())
print("La suma de todos los numeros primos por debajo de 2 millones es: "+str(sumaNumerosPrimos))           