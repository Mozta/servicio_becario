archivo=open("Axolotl.txt","r+")
content=archivo.read()
finDelArchivo=archivo.tell()

archivo.seek(finDelArchivo)
newContent=archivo.read()

TextoLimpio=("el azar me llevó hasta ellos una mañana de primavera en que parís abría su cola de pavo real después de la lenta invernada. Bajé por el bulevar de rort royal, tomé st. marcel y l’hôpital, vi los verdes entre tanto gris y me acordé de los leones. era amigo de los leones y las panteras, pero nunca había entrado en el húmedo y oscuro edificio de los acuarios. dejé mi bicicleta contra las rejas y fui a ver los tulipanes. los leones estaban feos y tristes y mi pantera dormía. opté por los acuarios, soslayé peces vulgares hasta dar inesperadamente con los axolotl. me quedé una hora mirándolos, y salí incapaz de otra cosa.")
Palabras=["a,ante,bajo,con,de,desde,durante,en,entre,excepto,hacia,hasta,mediante,para,por,salvo,segun,sin,sobre,tras"]

ListaPalabras=TextoLimpio.split()

CantidadPalabras0=[]
for Palabras in ListaPalabras:
    CantidadPalabras0.append(ListaPalabras.count("a"))

CantidadPalabras1=[]
for Palabras in ListaPalabras:
    CantidadPalabras1.append(ListaPalabras.count("ante"))

CantidadPalabras2=[]
for Palabras in ListaPalabras:
    CantidadPalabras2.append(ListaPalabras.count("bajo"))

CantidadPalabras3=[]
for Palabras in ListaPalabras:
    CantidadPalabras3.append(ListaPalabras.count("con"))

CantidadPalabras4=[]
for Palabras in ListaPalabras:
    CantidadPalabras4.append(ListaPalabras.count("de"))

CantidadPalabras5=[]
for Palabras in ListaPalabras:
    CantidadPalabras5.append(ListaPalabras.count("desde"))

CantidadPalabras6=[]
for Palabras in ListaPalabras:
    CantidadPalabras6.append(ListaPalabras.count("durante"))

CantidadPalabras7=[]
for Palabras in ListaPalabras:
    CantidadPalabras7.append(ListaPalabras.count("en"))

CantidadPalabras8=[]
for Palabras in ListaPalabras:
    CantidadPalabras8.append(ListaPalabras.count("entre"))

CantidadPalabras9=[]
for Palabras in ListaPalabras:
    CantidadPalabras9.append(ListaPalabras.count("excepto"))

CantidadPalabras10=[]
for Palabras in ListaPalabras:
    CantidadPalabras10.append(ListaPalabras.count("hacia"))

CantidadPalabras11=[]
for Palabras in ListaPalabras:
    CantidadPalabras11.append(ListaPalabras.count("hasta"))

CantidadPalabras12=[]
for Palabras in ListaPalabras:
    CantidadPalabras12.append(ListaPalabras.count("mediante"))

CantidadPalabras13=[]
for Palabras in ListaPalabras:
    CantidadPalabras13.append(ListaPalabras.count("para"))

CantidadPalabras14=[]
for Palabras in ListaPalabras:
    CantidadPalabras14.append(ListaPalabras.count("por"))

CantidadPalabras15=[]
for Palabras in ListaPalabras:
    CantidadPalabras15.append(ListaPalabras.count("salvo"))

CantidadPalabras16=[]
for Palabras in ListaPalabras:
    CantidadPalabras16.append(ListaPalabras.count("segun"))

CantidadPalabras17=[]
for Palabras in ListaPalabras:
    CantidadPalabras17.append(ListaPalabras.count("sin"))

CantidadPalabras18=[]
for Palabras in ListaPalabras:
    CantidadPalabras18.append(ListaPalabras.count("sobre"))

CantidadPalabras19=[]
for Palabras in ListaPalabras:
    CantidadPalabras19.append(ListaPalabras.count("tras"))

print("Texto normal\n" + TextoLimpio +"\n")
print("Palabras en lista\n" + str(ListaPalabras) +"\n")
print("Preposiciones 'a'\n" + str(CantidadPalabras0) +"\n")
print("Preposiciones 'ante'\n" + str(CantidadPalabras1) +"\n")
print("Preposiciones 'bajo'\n" + str(CantidadPalabras2) +"\n")
print("Preposiciones 'con'\n" + str(CantidadPalabras3) +"\n")
print("Preposiciones 'de'\n" + str(CantidadPalabras4) +"\n")
print("Preposiciones 'desde'\n" + str(CantidadPalabras5) +"\n")
print("Preposiciones 'durante'\n" + str(CantidadPalabras6) +"\n")
print("Preposiciones 'en'\n" + str(CantidadPalabras7) +"\n")
print("Preposiciones 'entre'\n" + str(CantidadPalabras8) +"\n")
print("Preposiciones 'excepto'\n" + str(CantidadPalabras9) +"\n")
print("Preposiciones 'hacia'\n" + str(CantidadPalabras10) +"\n")
print("Preposiciones 'hasta'\n" + str(CantidadPalabras11) +"\n")
print("Preposiciones 'mediante'\n" + str(CantidadPalabras12) +"\n")
print("Preposiciones 'para'\n" + str(CantidadPalabras13) +"\n")
print("Preposiciones 'por'\n" + str(CantidadPalabras14) +"\n")
print("Preposiciones 'salvo'\n" + str(CantidadPalabras15) +"\n")
print("Preposiciones 'segun'\n" + str(CantidadPalabras16) +"\n")
print("Preposiciones 'sin'\n" + str(CantidadPalabras17) +"\n")
print("Preposiciones 'sobre'\n" + str(CantidadPalabras18) +"\n")
print("Preposiciones 'tras'\n" + str(CantidadPalabras19) +"\n")

archivo.close()
print(newContent)
