from cgi import print_arguments


segundos=input("ingrese los segundos a convertir:")
segundos=int(segundos)

horas = segundos//3600 

sobrante1 = segundos%3600

minutos = sobrante1//60

sobrante2 = sobrante1%60

print("las horas son:",horas)


print("los minutos son:",minutos)


print("los segundos son:",sobrante2)


