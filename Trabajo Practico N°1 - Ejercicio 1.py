def dormimos(dia_semana, vacaciones):
    if dia_semana == False and vacaciones == False:
        return True
    elif dia_semana == True and vacaciones == False:
        return False
    else:
        return True
dia = str(input("¿Que dia es?: "))
vaca = str(input("¿Estas de vacaciones?(Si/No): "))
if dia == "lunes" or "martes" or "miercoles" or "martes" or "miercoles" or "jueves" or "viernes":
    dia = True
else:
    dia = False
if vaca == "Si":
    vaca = True
else:
    vaca = False
print(dormimos(dia,vaca))