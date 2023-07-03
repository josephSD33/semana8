numero1=float(input("Ingrese el primero numero "))
numero2=float(input("Ingrese el segundo numero "))
opcion=input("Ingrese S para sumar, R para restar o M para multiplicar ")
opcion=opcion.upper()
if opcion == "S":
    resultado= numero1+ numero2
elif opcion == "R":
    resultado= numero1 - numero2
elif opcion == "M":
    resultado= numero1 * numero2
else:
    print(" solo S, R o M")
print(f"El resultado es {resultado}")