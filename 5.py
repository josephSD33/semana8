horas=float(input('Ingrese las horas trabajadas '))
pago=float(input("Ingrese el pago por hora "))
jornada=48
if horas<=jornada:
    pagofinal= horas * pago
else:
    extras=horas-jornada
    pagoextras=extras*pago*2
    pagofinal=jornada*pago + pagoextras
print(F"El pago es de {pagofinal}")
    