# 1) Lista de notas de 10 estudiantes
notas = [8, 7.5, 9, 6.5, 10, 7, 8.5, 9.5, 6, 7]
print("Lista de notas:", notas)
promedio = sum(notas)/len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# 2) Lista de productos
productos = []
for i in range(5):
    p = input("Ingrese producto: ")
    productos.append(p)

print("Productos ordenados:", sorted(productos))
elim = input("Que producto desea eliminar? ")
if elim in productos:
    productos.remove(elim)
print("Lista actualizada:", productos)

# 3) Lista de 15 numeros aleatorios
numeros = [random.randint(1,100) for _ in range(15)]
pares = [n for n in numeros if n%2==0]
impares = [n for n in numeros if n%2!=0]
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# 4) Lista sin repetidos
valores = [1,2,3,2,4,5,3,6,1]
sin_repetidos = list(set(valores))
print("Lista sin repetidos:", sin_repetidos)

# 5) Lista de estudiantes con agregar/eliminar
estudiantes = ["Ana", "Juan", "Pedro", "Lucia", "Marta", "Diego", "Sofia", "Carlos"]
accion = input("Desea agregar o eliminar un estudiante? (agregar/eliminar): ")
if accion == "agregar":
    nuevo = input("Nombre del estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    elim = input("Nombre a eliminar: ")
    if elim in estudiantes:
        estudiantes.remove(elim)
print("Lista final:", estudiantes)

# 6) Rotar lista de 7 numeros a la derecha
nums = [1,2,3,4,5,6,7]
nums = [nums[-1]] + nums[:-1]
print("Lista rotada:", nums)

# 7) Matriz 7x2 temperaturas min y max
temperaturas = [[random.randint(10,20), random.randint(21,35)] for _ in range(7)]
prom_min = sum([t[0] for t in temperaturas])/7
prom_max = sum([t[1] for t in temperaturas])/7
amplitud = [t[1]-t[0] for t in temperaturas]
dia_amplitud = amplitud.index(max(amplitud)) + 1
print("Promedio min:", prom_min)
print("Promedio max:", prom_max)
print("Dia mayor amplitud:", dia_amplitud)

# 8) Notas de 5 estudiantes en 3 materias
notas_materias = [[random.randint(5,10) for _ in range(3)] for _ in range(5)]
for i, est in enumerate(notas_materias):
    print(f"Promedio estudiante {i+1}:", sum(est)/3)
for j in range(3):
    print(f"Promedio materia {j+1}:", sum([est[j] for est in notas_materias])/5)

# 9) Tablero Ta-Te-Ti
tablero = [["-" for _ in range(3)] for _ in range(3)]
for turno in range(2):  # solo 2 turnos como ejemplo
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    simbolo = "X" if turno%2==0 else "O"
    tablero[fila][col] = simbolo
    for fila_tab in tablero:
        print(fila_tab)

# 10) Ventas de 4 productos durante 7 dias
ventas = [[random.randint(1,20) for _ in range(7)] for _ in range(4)]
for i, prod in enumerate(ventas):
    print(f"Total producto {i+1}:", sum(prod))
ventas_dias = [sum([ventas[p][d] for p in range(4)]) for d in range(7)]
print("Dia con mayores ventas:", ventas_dias.index(max(vent
