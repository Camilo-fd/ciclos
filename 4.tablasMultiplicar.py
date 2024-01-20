for numero in range(1, 11):
    variable = ""
    for i in range (1, 11):
        resultado = numero * i
        if resultado < 10:
            variable += f"  {resultado} "
        elif resultado < 100:
            variable += f" {resultado} "
        else:
            variable += f"{resultado} "
    print(variable)