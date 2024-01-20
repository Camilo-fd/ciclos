tiempo = 0
continuar = True

while continuar:
    tramo = int(input("Ingrese el tiempo de viaje del tramo en minutos (0 para finalizar): "))
    if tramo == 0:
        break
    tiempo += tramo

horas = tiempo // 60
minutos = tiempo % 60

print (f"Tiempo total de viaje: {horas} : {minutos}")