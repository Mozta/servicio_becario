print(" Calculadora")
print("Elige un opción")
print("1-Suma")
print("2-Resta")
print("3-Multiplicación")
x= input("Escribe tu elección:")
y=float(x)

if(y==1):
  a=input("Primer número\n")
  b=input("Segundo número\n")
  a2=float(a)
  b2=float(b)
  resultado= a2+b2
  print("El resultado es:",resultado)
elif(y==2):
  a=input("Primer número\n")
  b=input("Segundo número\n")
  a2=float(a)
  b2=float(b)
  resultado= a2-b2
  print("El resultado es:",resultado)
elif(y==3):
  a=input("Primer número\n")
  b=input("Segundo número\n")
  a2=float(a)
  b2=float(b)
  resultado= a2*b2
  print("El resultado es:",resultado)
else:
  print("no valido")
