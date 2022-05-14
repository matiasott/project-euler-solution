"""
Comenzando con el número 1 y moviéndose hacia la derecha en el sentido de las agujas del reloj, se forma una espiral de 5 por 5 de la siguiente manera:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

Se puede verificar que la suma de los números de las diagonales es 101.

¿Cuál es la suma de los números en las diagonales en una espiral de 1001 por 1001 formada de la misma manera?

"""

import math

matriz= []
tamaño=1001
desimal, entera=math.modf(tamaño/2)
medio=int(entera)
for i in range(tamaño):
    matriz.append([0]*tamaño)
  
cantidadDeNumInMatriz=tamaño**2
matriz[medio][medio] = 1
f=medio
c=medio      

def cantidadFuncion(orientacion,valor):
    global contador
    if orientacion == "E" and contador<=cantidadDeNumInMatriz:
        este(valor)
        
    if orientacion == "S"and contador<=cantidadDeNumInMatriz:
        sur(valor)
             
    if orientacion == "O"and contador<=cantidadDeNumInMatriz:
        oeste(valor)
        
    if orientacion == "N"and contador<=cantidadDeNumInMatriz:
        norte(valor) 
           
contador=2
valorEste=1
valorSur=1
valorOeste=2
valorNorte=2
variableOrientacion="E"  

def giroDeLosDatos():
    global contador
    global valorEste
    global valorSur
    global valorOeste
    global valorNorte
    global variableOrientacion
    global f
    global c
    
    swich_orden={"E":"S","S":"O","O":"N","N":"E"}
      
    while contador <= cantidadDeNumInMatriz :
              
            
        
        #print(matriz)
        if variableOrientacion=="E":
            cantidadFuncion("E",valorEste)            
            
        if variableOrientacion=="S":
            cantidadFuncion("S",valorSur)            
            
        if variableOrientacion=="O":
            cantidadFuncion("O",valorOeste)            
            
        if variableOrientacion=="N":
            cantidadFuncion("N",valorNorte)            
            
        variableOrientacion=swich_orden[variableOrientacion]
        
        
def este(valiu):    
    global valorEste
    for i in range(valiu):        
        global f
        global c
        global contador
        global matriz
        if  contador<=cantidadDeNumInMatriz:                   
            f=f
            c=c+1
            matriz[f][c]=contador                   
            contador=contador+1            
                  
    if valorEste<=tamaño-1:
        valorEste = valorEste +2
    if valorEste==tamaño-1:
        valorEste=valorEste+1    
    

def sur(valiu):    
    global valorSur
    for i in range(valiu):        
        global f
        global c
        global contador
        global matriz
        f=f+1
        c=c
        matriz[f][c]=contador
        contador=contador+1        
    valorSur = valorSur +2 
        

def oeste(valiu):    
    global valorOeste
    for i in range(valiu):
        global f
        global c
        global contador
        global matriz
        f=f
        c=c-1
        matriz[f][c]=contador
        contador=contador+1        
    valorOeste = valorOeste +2  

def norte(valiu):    
    global valorNorte
    for i in range(valiu):
        global f 
        global c
        global contador
        global matriz
        f=f-1
        c=c
        matriz[f][c]=contador
        contador=contador+1    
    valorNorte = valorNorte +2 
   
        
giroDeLosDatos()

sumDiagPr= sum(matriz[i][i] for i in range(tamaño))

SumDiaSec=sum(matriz[i][tamaño-i-1] for i in range(tamaño))

Resultado=sumDiagPr+SumDiaSec-1
print(Resultado)
     
        




   
 
    

   
    
    
   
