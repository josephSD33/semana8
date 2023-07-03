ladoA=float(input("ingrese la medida del lado A "))
ladoB=float(input("ingrese la medida del lado B "))
ladoC=float(input("ingrese la medida del lado C "))

if ladoA**2 == ladoB**2 + ladoC**2 or ladoB**2 == ladoA**2 + ladoC**2 or ladoC**2 == ladoA**2 + ladoB**2:
    print("Es un triángulo rectángulo.")
elif ladoA==ladoB==ladoC:
    print("Es un triangulo equilatero")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("Es un triangulo isosceles")
else: 
    print("Es un triangulo escaleno")