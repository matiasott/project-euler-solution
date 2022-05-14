"""
Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.

Encuentra el palíndromo más grande formado por el producto de dos números de 3 dígitos.


"""


listaRango=list(reversed(range(100,1000)))
diccionarioMutiplicacion={}

def buscaValores():
    
    for i in listaRango:
        for j in listaRango:
            m=i*j
            lis_m=list(str(m))
            if lis_m == lis_m[::-1]:
                diccionarioMutiplicacion[i*j]=[i,j]        

buscaValores()
mayorKey=max(diccionarioMutiplicacion.keys())
num1=diccionarioMutiplicacion[mayorKey][0]
num2=diccionarioMutiplicacion[mayorKey][1]
print(" El Numero 1 es: " + str(num1) + " y el Numero 2 es: " + str(num2) + " y su multilicacion es el Numero capicua siguiente: " + str(num1*num2))

