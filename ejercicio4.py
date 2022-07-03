num=input("ingrese un numero de 3 sifras:")

num1 = int(num [0])
num2 = int(num [1])
num3 = int(num [3])


condicion1 = (num1 > num3)and (num1<num2)
condicion2 = (num1%2 == 0) or (num2%2 == 0) or (num3%2 == 0)
resultado = condicion1 and condicion2
print(resultado)