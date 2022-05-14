'''
El número de 5 dígitos, 16807 = 7*5 , también es una quinta potencia. De manera similar, el número de 9 dígitos, 134217728 = 8*9 , es una novena potencia.

¿Cuántas n -dígitos existen enteros positivos que son también un n º potencia?

'''

lis=[]
for i in range(1,10):
    for j in range(1,1000):
        if len(str(i**j))==j:
           lis.append(str(i)+"**"+str(j))
           
           
print(len(lis)) 


        


