def problema_loro(hablando,hora):
    if hablando == True and hora <= 7 or hora >= 20:
        return True
    else:
        return False
a = str(input("¿El loro esta hablando?(Si/No): "))
b = int(input("¿Que hora es?: "))
if b < 0 or b > 24:
    print("El horario no es valido")
    while b < 0 or b > 24:
        b = int(input("¿Que hora es?: "))
if a == "Si":
    a = True
else:
    a = False
print(problema_loro(a,b))