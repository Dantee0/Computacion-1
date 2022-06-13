def diferencia21(a):
    if a <= 21:
        diferencia = 21-a
        print(diferencia)
    else:
        diferencia2 = (21-a)*2
        print(diferencia2)
a = int(input("Ingresar el valor de a: "))
print(diferencia21(a))