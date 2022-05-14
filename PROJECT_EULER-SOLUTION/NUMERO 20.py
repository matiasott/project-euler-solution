"""
n ! significa n × ( n - 1) × ... × 3 × 2 × 1

Por ejemplo, ¡10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, ¡
y la suma de los dígitos del número 10! es 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

¡Encuentra la suma de los dígitos del número 100!

"""
valor = 100
for x in list(reversed(range(1,100))):
    valor = valor * x
suma = 0    
for i in str(valor):
    suma = suma + int(i)

print(suma)