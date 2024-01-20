numero_ingresado = int(input("Ingrese un número entero: "))
secuencia = [numero_ingresado]

while numero_ingresado != 1:
    if numero_ingresado % 2 == 0:
        numero_ingresado = numero_ingresado // 2
    else:
        numero_ingresado = 3 * numero_ingresado + 1
    secuencia.append(numero_ingresado)

print(f"Secuencia de Collatz  {secuencia}")