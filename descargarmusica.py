import pytube 
link = input ("ingrese ele link del video:")
youlink = pytube.YouTube(link)
print("titulo:",youlink.title)
print("Autor:",youlink.author)
youlink.streams.filter(abr="160kbps",progressive=False).first().download(filename="audio.mp3")
print("Descarga exitosa de :",link)