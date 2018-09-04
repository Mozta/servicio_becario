import time
nombre=input("Dime tu nombre")
print("Bienvenido,"+nombre,"Jugaras algo que ya conoces, ahorcado, adivina la palabra")
print("")
time.sleep(1)
print("Comenzamos")
time.sleep(0.5)
palabra='cctmexico'
tupalabra=''
vidas=5

while vidas > 0:
  fallas=0
  for  letra in palabra:
      if letra in tupalabra:
          print(letra,end="")
       else:
           print("*",end="")
           fallas+=1

    if fallas==0:
        print("Felicidades, ganaste")
        break
    
    tuletra=input("Introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("Esa letra no es")
        print("Te quedan ",+vidas," vidas")
    if vidas ==0:
        print("Perdiste jaja")

else:
    print("Gracias por jugar")

    

