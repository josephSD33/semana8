edad=int(input("Ingrese su edad "))
if edad<4:
    precio=0
elif edad<=18:
    precio=5
elif edad>18:
    precio=10
print(F"El cliente debe pagar {precio}€")