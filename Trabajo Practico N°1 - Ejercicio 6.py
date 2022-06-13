def hacer10(a,b):
    sum = a + b
    if sum == 10 or a == 10 or b == 10:
        return True
    else:
        return False
num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))
print(hacer10(num1,num2))