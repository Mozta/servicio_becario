r=True
n=int(input("Ingresar numero\n"))
d=0
while d<n and r:
    if n%2==0:
        r=False
    d=d+1
if(r):
    print("El numero ingresado es primo")
else:
    print("El numero ingresado NO es primo")
