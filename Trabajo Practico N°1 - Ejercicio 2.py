def problemas_monos(a_sonriendo, b_sonriendo):
    if a_sonriendo == True and b_sonriendo == True:
        return True
    else:
        if a_sonriendo == False and b_sonriendo == False:
            return True
        else:
            if a_sonriendo == True and b_sonriendo == False:
                return False
a = str(input("El mono a, ¿Esta sonriendo?(Si/No): "))
b = str(input("El mono b, ¿Esta sonriendo?(Si/No): "))
if a == "Si":
    a = True
else:
    a = False
if b == "Si":
    b = True
else:
    b = False
print(problemas_monos(a,b))