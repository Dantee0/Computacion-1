def pos_negativa(a,b,negativa):
    if a >= 0 and b < 0 and negativa == False:
        return True
    elif a < 0 and b >= 0 and negativa == False:
        return True
    else:
        return False
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
if num1 < 0 and num2 < 0:
    valor = True
else:
    valor = False
print(pos_negativa(num1,num2,valor))