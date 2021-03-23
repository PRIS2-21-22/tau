polinomioUno = []
polinomioDos = []
resultado = []

def suma():
    i=0
    while i<=int(Grado):
        resultado.append(polinomioUno[i]+polinomioDos[i])
        i += 1
    print(f"Has invocado la suma, cuyo resultado es {resultado}")

def resta():
    i=0
    while i<=int(Grado):
        resultado.append(polinomioUno[i]-polinomioDos[i])
        i += 1
    print(f"Has invocado la resta, cuyo resultado es {resultado}")


def multiplicacion():
    i=0
    while i<=int(Grado):
        resultado.append(polinomioUno[i]*polinomioDos[i])
        i += 1
    print(f"Has invocado la multiplicacion, cuyo resultado es {resultado}")



print("¿Hasta que grado van a llegar los polinomios?")
Grado = int(input())

print("--Rellenando los valores del primer polinomio--")
i=0
aux=0
while i<=Grado:
    print(f"Introduce el valor para el grado {Grado - i}")
    polinomioUno.append(int(input()))
    i += 1


print("--Rellenando los valores del segundo polinomio--")
i=0
while i<=Grado:
    print(f"Introduce el valor para el grado {Grado - i}")
    polinomioDos.append(int(input()))
    i += 1


print("¿Que quieres hacer con los polinomios? \n 0 = Sumarlos \n 1 = Restar al primero el segundo \n 2 = Multiplicar")
cuenta=int(input())

if cuenta==0:
    suma()
if cuenta==1:
    resta()
if cuenta==2:
    multiplicacion()






