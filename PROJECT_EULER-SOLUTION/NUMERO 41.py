'''

Problema 41

Diremos que un número de n dígitos es pandigital si utiliza todos los dígitos del 1 al n exactamente una vez. Por ejemplo, 2143 es un pandigital de 4 dígitos y también es primo.

¿Cuál es el primo pandigital de n dígitos más grande que existe?


'''




from itertools import permutations

numeros_Lista=[9,8,7,6,5,4,3,2,1]

def esPrimo(num):    
    if num == 0: return False
    if num <= 3: return True
    i = 2
    while i * i < num + 1:
        if num % i == 0: return False
        i += 1
    return True

def encuentra_numero(lista):    
    perm = permutations(lista)
    num = ''
    num_entero=0    
    for k in list(perm):          
        for j in k:
            num=str(num)+str(j)
            if len(num)==len(lista):                
                num_entero=int(num)                
                if esPrimo(num_entero):   
                    num=''
                    return num_entero                    
                else:
                    num = ''
                    num_entero=0
    return 0
    
def logica():
    valor=0    
    valor=encuentra_numero(numeros_Lista)
    if valor!=0:
        return valor  
    else:
        for i in range(8):                
            if valor==0:
                numeros_Lista.remove(numeros_Lista[0])               
                valor=encuentra_numero(numeros_Lista)
                if valor!=0:
                    return valor

valorete=logica()
print("El Numero buscado es: ",valorete)
print ("fin")





