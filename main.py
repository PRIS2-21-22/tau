#Declaracion de las listas que vamos a usar
polinomioUno = []
polinomioDos = []
resultado = []

#Metodo de suma
#Acepta dos polinomios distintos y los suma en un tercero
def suma():
    i=0
    while i<=int(Grado):
        resultado.append(polinomioUno[i]+polinomioDos[i])
        i += 1
    print(f"Has invocado la suma, cuyo resultado es (De mayor a menor grado) {resultado}")

#Metodo de resta
#Acepta dos polinomios distintos y los resta en un tercero
def resta():
    i=0
    while i<=int(Grado):
        resultado.append(polinomioUno[i]-polinomioDos[i])
        i += 1
    print(f"Has invocado la resta, cuyo resultado es (De mayor a menor grado) {resultado}")

#Metodo de multiplicacion
#Acepta dos polinomios distintos y los multiplica en un tercero de longitud grado + grado
#Invertimos el array por comodidad a la hora de hacer las cuentas
#Gracias a la inversion, la i y la j a parte de valer para los bucles, valen para saber que grado tienen cada elemento de la lista
#Creamos una lista vacia de longitud igual al grado máximo que podrá alcanzar (Grado + Grado)
#Ahora recorremos la lista 2 con cada uno de los valores de la lista 1 y en cada iteracion de j, el resultado irá al grado i + j, sumando
#Al final volvemos a invertir el resultado para que vaya de mayor a menor grado
def multiplicacion():
    i=0
    polinomioUno.reverse()
    polinomioDos.reverse()

    while i<=Grado + Grado:
        resultado.append(0)
        i += 1
    
    i=0

    while i<=Grado:
        j=0
        while j<=Grado:
            resultado[i+j]=resultado[i+j] + (polinomioUno[i]*polinomioDos[j])
            j+=1
        i+=1

    resultado.reverse()
    
    print(f"Has invocado la multiplicacion, cuyo resultado es (De mayor a menor grado): {resultado}")


#Pedimos por pantalla el grado maximo al que van a llegar los polinomios
print("¿Hasta que grado van a llegar los polinomios?")
Grado = int(input())

#Rellenamos el primero
print("--Rellenando los valores del primer polinomio--")
i=0
aux=0
while i<=Grado:
    print(f"Introduce el valor para el grado {Grado - i}")
    polinomioUno.append(int(input()))
    i += 1

#Rellenamos el segundo
print("--Rellenando los valores del segundo polinomio--")
i=0
while i<=Grado:
    print(f"Introduce el valor para el grado {Grado - i}")
    polinomioDos.append(int(input()))
    i += 1

#Pedimos la operacion que se va a usar
print("¿Que quieres hacer con los polinomios? \n 0 = Sumarlos \n 1 = Restar al primero el segundo \n 2 = Multiplicar")
cuenta=int(input())

if cuenta==0:
    suma()
if cuenta==1:
    resta()
if cuenta==2:
    multiplicacion()






