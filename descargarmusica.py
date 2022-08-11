import pytube 

opcion = int (input("selecione una opcion \n1-Descargar musica \n2-salir \n"))

while opcion !=2:

    link = input ("ingrese ele link del video:")
    youlink = pytube.YouTube(link)
    print("titulo:",youlink.title)
    print("Autor:",youlink.author)
    youlink.streams.filter(abr="160kbps",progressive=False).first().download(filename="audio.mp3")
    print("Descarga exitosa de :",link)

    
    opcion = int (input("selecione una opcion \n1-Descargar musica \n2-salir \n"))
