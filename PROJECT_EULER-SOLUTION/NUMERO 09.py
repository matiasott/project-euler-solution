"""
Un triplete pitagórico es un conjunto de tres números naturales, a < b < c , para los cuales,

a 2 + b 2 = c 2
Por ejemplo, 3 2 + 4 2 = 9 + 16 = 25 = 5 2 .

Existe exactamente un triplete pitagórico para el cual a + b + c = 1000.
Halla el producto abc .

"""

def calcula():
    for a in range(1000):
        for b in range((1000)):
            if a+b<1000 and a!=0 and b!=0:       
                if a**2+b**2==(1000-a-b)**2:
                    c=1000-a-b
                    return a,b,c,a*b*c

v=calcula()
print("El valor del producto es: " + str(v[3])+ " y los valores de los catetos son: " + str(v[0])+ " y "+ str(v[1])+ " y el de su hipotenusa es: "+str(v[2]) )
