"""
Al enumerar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el sexto primo es 13.

¿Cuál es el número primo 10001er?

"""

import itertools
lista=[]

def esPrimo(num):
    if num == 0: return False
    if num <= 3: return True
    i = 2
    while i * i < num + 1:
        if num % i == 0: return False
        i += 1
    return True


def anexa():
    for n in itertools.count(1):        
        if esPrimo(n) and n != 1:
           lista.append(n)
           if len(lista)==10001:
               return             

anexa()
print("El numero primo en la posicion 10001 es: "+str(lista[-1]))


