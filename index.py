with open("informacion.txt" ,"r", encoding="utf-8") as file:
    lineas = file.readlines()[1:]

for i, linea in enumerate(lineas, start=1):
    print(linea.strip())
