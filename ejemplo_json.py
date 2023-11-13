import json

#Crea un menú con las opciones de agendar contacto y ver información de contacto. OK
#Para agendar se solicitará al usuario: nombre, apellido, teléfono, dirección. OK
#Para ver informacion se pedirá el nombre y apellido.
#La información será un listado de diccionarios, donde cada diccionario tendrá como claves lo
#solicitado al usuario y como valor lo que ingrese el usuario. A su vez, este listado debe estar
#guardado en un archivo JSON.

import json

select = ""

def guardar_contacto():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")    
    
    nuevo_contacto = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Telefono": telefono,
        "Dirección": direccion
    }
    
    with open("agenda.txt", "a") as archivo:
        json.dump(nuevo_contacto, archivo, indent=4)
        
    print(f"El contacto {nombre} {apellido} ha sido agendado correctamente")

def traer_contacto():
    pass

def menu():
    print("1. Agendar contacto")
    print("2. Ver información de contacto")
    print("3. Salir")
    global select  
    select = input("Opción: ")
    
while True:
    menu()
    if select == "1":
        guardar_contacto()
    elif select == "2":
        traer_contacto()
    elif select == "3":
        print("Adiós")
        break
    else:
        print("Ingresar opción válida")

