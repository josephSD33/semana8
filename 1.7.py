edad=int(input("ingrese su edad "))
ingresos=float(input("ingrese la cantidad de dinero que gana mensualmente "))
if edad>16 and ingresos >= 1000:
    print("el usuario puede tributar")
else:
    print("el usuario no puede tributar")