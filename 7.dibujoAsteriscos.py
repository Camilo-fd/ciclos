opcion = input("\n1. altura y el ancho de un rectángulo\n2. triángulo del tamaño indicado\n3. hexágono del tamaño indicado\n")

if opcion == "1":
    
    altura = int(input("altura: "))
    ancho = int(input("ancho: "))

    for i in range(altura):   
        variable = "*" * ancho
        print(variable)
elif opcion == "2":
    altura = int(input("altura: "))

    for i in range(1, altura+1):
        variable = "*" * i
        print(variable)
elif opcion == "3":
    print("No fui capaz de hacerlo")