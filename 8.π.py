n = int(input("numero: "))

suma = 0

# Calcular la estimación de π utilizando un ciclo for
for i in range(n):
    termino = ((-1) ** i) * 4 / (2 * i + 1)
    suma += termino
print(suma)