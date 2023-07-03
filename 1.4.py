print("Candidato A del partido rojo")
print("Candidato b del partido verde")
print("Candidato c del partido azul")
voto=input("Ingrese A para votar por el partido rojo, B para votar por el partido verde o C para votar por el azul ")
voto=voto.upper()
if voto== "A":
    print('Usted ha votado por el partido rojo')
elif voto=="B":
    print('Usted ha votado por el partido verde')
elif voto=="C":
    print('Usted ha votado por el partido azul')
else:
    print("opcion erronea")