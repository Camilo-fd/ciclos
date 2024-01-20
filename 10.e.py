import math
e = 0
n = 0

while True:
    termino = 1 / math.factorial(n)
    e_anterior = e
    e += termino

    if abs(e - e_anterior) < 0.0001:
        break

    n += 1

print(f"e es igual: {e}")