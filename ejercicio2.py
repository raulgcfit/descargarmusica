URL= input("ingrese URL empresarial:")
nombre1=input("ingrese su nombre:")
nombre2=input("ingrese segindo nombre:")
apellido1=input("ingrese primer apellido:")
aprellido2=input("ingrese segundo apellido:")
year=input("ingrese año de nacimiento:")

letra1=nombre1[0]
letra2=nombre2[0]
#conseguir ultimos dos numeros
ultiNum=year[2:]
#slicing
nomEmp=URL[4:-4]
correo=letra1+letra2+apellido1+ultiNum+"@"+nomEmp+".com"
print("su correo empresarial es : {}".format(correo))