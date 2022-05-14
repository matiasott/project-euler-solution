"""
Los números primos 3, 7, 109 y 673 son bastante notables.
 
Al tomar dos números primos y concatenarlos en cualquier orden, el resultado siempre será primo.
Por ejemplo, tomando 7 y 109, tanto 7109 como 1097 son primos. 

La suma de estos cuatro números primos, 792, representa la suma 
más baja para un conjunto de cuatro números primos con esta propiedad.

Encuentre la suma más baja para un conjunto de cinco primos para los
 cuales dos primos cualesquiera se concatenan para producir otro primo.
 """
diccionario_Final={}
def esPrimo(num):
    if num == 0: return False
    if num <= 3: return True
    i = 2
    while i * i < num + 1:
        if num % i == 0: return False
        i += 1
    return True


def concatenaDosvalores(v1,v2):
    concatenado1=int(str(v1)+str(v2))
    concatenado2=int(str(v2)+str(v1))
    if esPrimo(concatenado1) and esPrimo(concatenado2): return True
    else: return False

def iterar():
    valorSuma=27000
    for i in range(3,valorSuma):
        if esPrimo(i):            
            num1=i
            print("num 1 "+ str(i)) 
            for j in range((i+1),valorSuma):
                if esPrimo(j) and (i+4*j)<valorSuma:                  
                    v11=concatenaDosvalores(i,j)
                    if v11:
                        num2=j                                         
                        for k in range((j+1),valorSuma):
                            if esPrimo(k) and (i+j+3*k)<valorSuma:
                                if concatenaDosvalores(i,k):  
                                    if concatenaDosvalores(j,k):  
                                        num3=k                                                             
                                        for w in range((k+1),valorSuma):
                                            if esPrimo(w) and (i+j+k+2*w)<valorSuma:
                                                if concatenaDosvalores(i,w):
                                                    if concatenaDosvalores(j,w):
                                                        if concatenaDosvalores(k,w):
                                                            num4=w                     
                                                            for x in range((w+1),valorSuma):
                                                                if esPrimo(x) and (i+j+k+w+x)<valorSuma:
                                                                    if concatenaDosvalores(i,x):
                                                                        if concatenaDosvalores(j,x):
                                                                            if concatenaDosvalores(k,x):
                                                                                if concatenaDosvalores(w,x):
                                                                                    num5=x
                                                                                    print("encontre "+ str(x))
                                                                                    suma=num1+num2+num3+num4+num5
                                                                                    diccionario_Final[suma]=[num1,num2,num3,num4,num5]
                                                                                    
                                                                                    



iterar()
print(diccionario_Final)
print("fin")

                   
            

