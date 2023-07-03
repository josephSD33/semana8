numero1= float(input("Ingrese el primer numero "))
numero2= float(input("Ingrese el segundo numero "))
eleccion=str(input("Escriba S para sumarlos, R para restarlos o M para multiplicarlos "))
if eleccion == "S":
    resultado= numero1 + numero2
    print(F'El resultado es {resultado}')

elif eleccion == "R":
    resultado= numero1 - numero2
    print(F'El resultado es {resultado}')  

elif eleccion == "M":
    resultado= numero1*numero2  
    print(F'El resultado es {resultado}')
  

