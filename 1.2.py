numero1=input("Ingrese el primer numero ")
numero2=input("ingrese el segundo numero ")

if numero1.isnumeric() and numero2.isnumeric():
    if numero1 == numero2:
        print("Los dos números son iguales")
    else:
        print("Los dos números son diferentes")
    if numero1 > numero2:
        print("El primer número es mayor que el segundo")
    else:
        print("El segundo numero es mayor o igual que el primero")
else:
    print("uno o ambos digitos son letra")
