numero1 = int(input("Escriba el primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))
suma = 0
for i in range(numero1+1,numero2):
    suma += i
print(suma)