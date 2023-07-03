palabra1=str(input("ingrese la primera palabra "))
palabra2=str(input("ingrese la segunda palabra "))
ultimas3d1=palabra1[-3:]
ultimas3d2=palabra2[-3:]
ultimas2d1=palabra1[-2:]
utilmas2d2=palabra2[-2:]
if ultimas3d1 == ultimas3d2:
    print("las palabras riman ")
elif ultimas2d1 == utilmas2d2:
    print("las riman un poco")
else:
    print('las palabras no riman')