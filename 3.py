salario= float(input("Ingrese el salrio diario del empleado "))
diastrab= float(input("Ingrese los dias trabajados por el empleado "))
salariototal= salario*diastrab
Dpension= salariototal*0.1
Dsalud= salariototal*0.15
salariofinal=salariototal-Dpension -Dsalud
print(F'El slario final del empleado es {salariofinal}')