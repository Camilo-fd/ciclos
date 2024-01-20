fraccion = 1.0
suma = 0.0
potencia = 1

print("Potencia  Fraccion  Suma")
print(f"{potencia}\t{fraccion}\t{suma}")

while fraccion > 0.000001:
    potencia += 1
    fraccion /= 2
    suma += fraccion
    print(f"{potencia}\t{fraccion}\t{suma}")
