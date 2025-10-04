# 1) Imprimir del 0 al 100
for i in range(101):
    print(i)

# 2) Contar cantidad de digitos
numero = input("Ingrese un numero entero: ")
print("Cantidad de digitos: ", len(numero))

# 3) Suma entre dos valores (excluyendo los extremos)
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(a+1, b):
    suma += i
print("Suma entre los valores: ", suma)

# 4) Suma de numeros ingresados hasta 0
total = 0
while True:
    n = int(input("Ingrese un numero (0 para salir): "))
    if n == 0:
        break
    total += n
print("Total acumulado: ", total)

# 5) Juego adivinar numero aleatorio
import random
num = random.randint(0,9)
intentos = 0
while True:
    adivina = int(input("Adivina el numero entre 0 y 9: "))
    intentos += 1
    if adivina == num:
        break
print("Adivinaste en ", intentos, "intentos")

# 6) Numeros pares de 100 a 0
for i in range(100, -1, -2):
    print(i)

# 7) Suma hasta numero ingresado
limite = int(input("Ingrese un numero positivo: "))
suma = 0
for i in range(limite+1):
    suma += i
print("Suma total: ", suma)

# 8) Clasificacion de 100 numeros
pares = impares = positivos = negativos = 0
for i in range(10): 
    n = int(input("Ingrese un numero: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    else:
        negativos += 1
print(pares, "pares", impares, "impares", positivos, "positivos", negativos, "negativos")

# 9) Media de 100 numeros
suma_total = 0
for i in range(10): 
    n = int(input("Ingrese un numero: "))
    suma_total += n
media = suma_total / 10
print("Media: ", media)

# 10) Invertir digitos de un numero
num = input("Ingrese un numero: ")
print("Numero invertido: ", num[::-1])
