with open("informacion.txt" ,"r", encoding="utf-8") as file:
    lineas = file.readlines()[1:]

for i, linea in enumerate(lineas, start=1):
    print(linea.strip())

print("---------------------")
lineas = [r.strip() for r in lineas]
print(lineas)
print("----------------------")

for l in lineas:
    print(l)

print("----------------------")
lineas = lineas[1:]
for l in lineas:
    apellido = l[0]
    if apellido[0] == "B":
        print(l)

