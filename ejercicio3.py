num1=int(input("ingrese numero 1:"))
num2=int(input("ingrese numero 2:"))

residuo= num1 % num2
condicion= residuo == 0
print("¿{} es divisible entre {}? {}".format(num1,num2,condicion))