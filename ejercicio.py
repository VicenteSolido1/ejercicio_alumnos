alumnos = []
import os
menu = """
1. ingrese alumno
2. ver alumno
3.salir""" 

while True:
    os.system("cls")
    print(menu)
    opc = input("Seleccione la opcion")
    os.system("cls")
    if opc =="1":
        nombre = input("ingrese el nombre del alumno: ")
        codigo = input("INGRESE EL CODIGO: ")
        edad = int(input("Ingrese la edad del alumno: "))
        alumno = {"codigo": codigo ,
                   "nombre": nombre ,
                   "edad": edad     }
        alumnos.appendappend(alumno)
    elif opc =="2":
        pass
    elif opc =="3":
        pass
    else:
        print("bye")

