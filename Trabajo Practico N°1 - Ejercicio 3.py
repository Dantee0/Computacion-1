def suma_double(a,b):
    if a == b:
        suma = (a+b) * 2
        print(suma)
    else:
        suma = a+b
        print(suma)
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
print(suma_double(a,b))