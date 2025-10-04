# 1) Edad mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2) Nota aprobada
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Números pares
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Categorías de edad
edad2 = int(input("Ingrese su edad: "))
if edad2 < 12:
    print("Niño/a")
elif edad2 >= 12 and edad2 < 18:
    print("Adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Contraseñas
clave = input("Ingrese una contraseña: ")
if len(clave) >= 8 and len(clave) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Moda, media y mediana
from statistics import mode, mean, median
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

m = mean(numeros_aleatorios)
md = median(numeros_aleatorios)
mo = mode(numeros_aleatorios)

if m > md and md > mo:
    print("Sesgo positivo")
elif m < md and md < mo:
    print("Sesgo negativo")
elif m == md == mo:
    print("Sin sesgo")
condiciones)

# 7) Palabra que termina en vocal
texto = input("Ingrese una palabra o frase: ")
if texto[-1] in "aeiou":
    print(texto + "!")
else:
    print(texto)

# 8) Opciones de nombre
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1, 2 o 3 segun la opción que desee: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else
    print("Opción incorrecta")   

# 9) Escala de Richter
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10) Estaciones del año
hemisferio = input("Ingrese hemisferio (N/S): ")
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
else:
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")
