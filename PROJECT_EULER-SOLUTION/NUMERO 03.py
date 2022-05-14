"""
Los factores primos de 13195 son 5, 7, 13 y 29.

¿Cuál es el factor primo más grande del número 600851475143?


"""


numeroReferencia=600851475143

lista=[]

def listaRango(num):
    listaRango = (range(1,num))
    return listaRango

def esPrimo(num):
    if num == 0: return False
    if num <= 3: return True
    i = 2
    while i * i < num + 1:
        if num % i == 0: return False
        i += 1
    return True

def buscaNumero():
    numero = 600851475143
    contador=True    
    multi=1
    for i in listaRango(numero):
        if contador:
            if (numero % i) == 0 :            
                if esPrimo(i):
                    lista.append(i)
                    numero=numero/i
                    multi=multi * (lista[-1])
                    if multi == numeroReferencia:
                        return
            

buscaNumero()
print("Los Multiples Primos son los siguiente: " + str(lista))
print("El numero buscado es: " +str(lista[-1]))

