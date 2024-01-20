numero = int(input("introduzca el numero: ")) 
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        print(divisor)
