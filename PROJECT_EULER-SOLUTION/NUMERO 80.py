'''
Es bien sabido que si la raíz cuadrada de un número natural no es un número entero, entonces es irracional. La expansión decimal de tales raíces cuadradas es infinita sin ningún patrón repetitivo.

La raíz cuadrada de dos es 1.41421356237309504880..., y la suma digital de los primeros cien dígitos decimales es 475.

Para los primeros cien números naturales, encuentre el total de las sumas digitales de los primeros cien dígitos decimales para todas las raíces cuadradas irracionales.

'''
import decimal

lista=list(range(1,101))
lista_sumas=[]
def raiznumeros(num):    
    suma=0
    k=0
    decimal.getcontext().prec = 105
    valor=decimal.Decimal(num).sqrt()    
    for i in str(valor):
        k=k+1        
        if k!=2 and k<102:
            suma=suma+int(i)
    lista_sumas.append(suma)
    print(lista_sumas)
    suma=0
    k=0

for i in lista:
    raiznumeros(i)    
valorBuscado=sum(lista_sumas)-1-1-2-3-4-5-6-7-8-9
print("El valor buscado es",valorBuscado)


