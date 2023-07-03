valorinicial=float(input("Ingrese el monto que debe pagar "))

if valorinicial >= 10000 and valorinicial <= 20000:
    descuento=valorinicial*0.1
elif valorinicial>=20001 and valorinicial <=50000:
    descuento= valorinicial*0.3
elif valorinicial>50000:
    descuento=valorinicial*0.5
else:
    descuento=0


preciofinal= valorinicial-descuento

print(F'Por el el valor de su compra se aplicara un descuento, el monto total a pagar es de {preciofinal}')
