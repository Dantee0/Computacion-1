def cerca_cien(n):
    if n in range(90,111) or n in range (190,211):
        return True
    else:
        return False
num = int(input("Ingrese un numero: "))
print(cerca_cien(num))