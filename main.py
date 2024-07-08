from os import system
from pacientes import *
from archivos import *

lista_pacientes = []
paciente_dado_de_alta = False

lista_pacientes = lectura_archivo("Pacientes.csv")

crear_archivo("Pacientes.csv", lista_pacientes)

if lista_pacientes is None:
    lista_pacientes = []

def mostrar_opciones() -> str :
    """Muestra un menu de opciones

    Returns:
        str: devuelve el menu 
    """
    opcion = input("MENU\n1. Dar de alta\n2. Modificar\n3. ELiminar\n4. Mostrar todos\n5. Ordenar pacientes\n6. Buscar paciente por DNI\n7. Calcular promedio\n8. Determinar compatibilidad\n9. Salir\nElija una opcion: ")
    return opcion

while True:
    opcion = mostrar_opciones()
    match opcion:
        case "1":
            dar_de_alta(lista_pacientes)
            paciente_dado_de_alta = True
        case "2":
            if paciente_dado_de_alta == True:
                dni = get_int("Ingrese el DNI del paciente a modificar: ", 4000000, 99999999)
                modificar_paciente(lista_pacientes, dni)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "3":
            if paciente_dado_de_alta == True:
                dni = get_int("Ingrese el DNI del paciente a eliminar: ", 4000000, 99999999)
                eliminar_paciente(lista_pacientes, dni)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "4":
            if paciente_dado_de_alta == True:
                mostrar_todos(lista_pacientes)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "5":
            if paciente_dado_de_alta == True:
                ordenar_pacientes(lista_pacientes)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "6":
            if paciente_dado_de_alta == True:
                dni = get_int("Ingrese el DNI del paciente a buscar: ", 4000000, 99999999)
                buscar_paciente_por_dni(lista_pacientes, dni)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "7":
            if paciente_dado_de_alta == True:
                resultado = calcular_promedio(lista_pacientes)
                print(resultado)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "8":
            if paciente_dado_de_alta == True:
                dni = get_int("Ingrese el DNI del paciente: ", 4000000, 99999999)
                determinar_compatibilidad(lista_pacientes, dni)
                matriz = crear_matriz(lista_pacientes)
                mostrar_matriz(matriz)
            else:
                print("Error, primero debe dar de alta un paciente")
        case "9":
            if confirmar_salida(lista_pacientes):
                break
        
    system("pause")
    system("cls")

