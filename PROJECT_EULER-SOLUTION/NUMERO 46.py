'''
Christian Goldbach propuso que todo número compuesto impar se puede escribir como la suma de un primo y el doble de un cuadrado.

9 = 7 + 2×1 al cuadrado 2
15 = 7 + 2×2 2
21 = 3 + 2×3 2
25 = 7 + 2×3 2
27 = 19 + 2×2 2
33 = 31 + 2×1 2

Resulta que la conjetura era falsa.

¿Cuál es el compuesto impar más pequeño que no se puede escribir como la suma de un número primo y el doble de un cuadrado?
'''
import math


Compuesto=9
verifica=True
ultimoCompuesto=9


def esPrimo(num):
    if num == 0: return False
    if num <= 3: return True
    i = 2
    while i * i < num + 1:
        if num % i == 0: return False
        i += 1
    return True

def esImpar(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
def cuadrado(num):
    return num * num

def esCopmpuesto(num):    
    if num == 0 or num == 1 or num % 2 == 0 :
        return False
    if esPrimo(num)==False and esImpar(num)== True:
        return True
        
def generaEntero(num):
    valor=math.ceil(num/2)
    return valor

def creaListadePrimosParaUnCompuesto(num):
    listaDePrimos=[]
    for i in range(num):
        if esPrimo(i):
            listaDePrimos.append(i)
    
    return listaDePrimos

def comprobacion(numCompuesto):
    global ultimoCompuesto
    listaPrimos=creaListadePrimosParaUnCompuesto(numCompuesto)
    rangovariable=list(range(generaEntero(numCompuesto)))
    for i in listaPrimos:
        for j in rangovariable:            
            if numCompuesto == i + 2 * cuadrado(j):
                ultimoCompuesto=numCompuesto
                return True
    else:
        ultimoCompuesto=numCompuesto
        print("El numero compuesto es:",ultimoCompuesto)
        global verifica         
        verifica = False   

while verifica == True:
    
    if esCopmpuesto(Compuesto) == True:        
        comprobacion(Compuesto)
        Compuesto=Compuesto+1
    else:  
        Compuesto=Compuesto+1



