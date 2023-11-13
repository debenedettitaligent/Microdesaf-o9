import os

def crear_tabla(numero):
    contenido =""
    for i in range(1, 11):
        resultado = numero * i
        contenido += f"{numero} X {i} = {resultado} \n"
        
        

    nombre_archivo = f"tabla_{numero}.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    
print(f"La tabla del {numero} ha sido generada y guardada")

def mostrar_tabla(numero)
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido de la tabla: \n {contenido}")
    except FileNotFoundError:
        print("No se ha encontrado")
        