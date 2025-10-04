
# 1) Hola Mundo
print("Hola Mundo!")

# 2) Saludo con nombre
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}! ")

# 3) Nombre, apellido, edad, lugar
nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su lugar de residencia: ")
print(f"Soy {nom} {ape}, tengo {edad} años y vivo en {pais}")

# 4) Área y perímetro de un círculo
radio = float(input("Ingrese el radio de un círculo: "))
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio
print(f"Área: {area}, Perímetro: {perimetro}")

# 5) Segundos a horas
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print("Equivale a", horas, "horas")

# 6) Tabla de multiplicar
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7) Operaciones con dos números
a = int(input("Ingrese el primer número (≠0): "))
b = int(input("Ingrese el segundo número (≠0): "))
print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicación:", a*b)
print("División:", a/b)

# 8) Índice de Masa Corporal (IMC)
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print(f"Su IMC es {imc:.2f}")

# 9) Conversión Celsius a Fahrenheit
c = float(input("Ingrese una temperatura en Celsius: "))
f = (9/5) * c + 32
print(f"Equivalente en Fahrenheit: {f}")

# 10) Promedio de 3 números
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
z = float(input("Ingrese el tercer número: "))
promedio = (x + y + z) / 3
print("El promedio es:", promedio)
