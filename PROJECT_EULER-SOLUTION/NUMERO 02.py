"""
Cada nuevo término en la secuencia de Fibonacci se genera sumando los dos términos anteriores. Al comenzar con 1 y 2, los primeros 10 términos serán:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Al considerar los términos en la secuencia de Fibonacci cuyos valores no exceden los cuatro millones, encuentre la suma de los términos pares.

"""


lista=[]
lista.append(1)
lista.append(2)
[lista.append(n) for n in range(3,4000000) if (lista[-1]+lista[-2]) == n]
l=[n for n in lista if n % 2 == 0]
print(sum(l))





