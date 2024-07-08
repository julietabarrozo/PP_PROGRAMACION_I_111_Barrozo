from input import *
from pacientes_secundarias import *

lista_ids = []

def crear_paciente(nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str) -> dict:
    """Crea un paciente en forma de diccionario

    Args:
        nombre (str): nombre del paciente
        apellido (str): apellido del paciente
        edad (int): edad del paciente
        altura (int): altura en cm del paciente
        peso (float): peso del paciente
        dni (int): dni del paciente
        grupo_sanguineo (str): grupo sanguineo del paciente

    Returns:
        dict: dict con los datos
    """
    contador_id = asignar_id(lista_ids)
    diccionario_pacientes = {
        "id" : contador_id,
        "nombre" : nombre,
        "apellido" : apellido,
        "edad" : edad,
        "altura" : altura,
        "peso" : peso,
        "dni" : dni,
        "grupo sanguineo" : grupo_sanguineo
    }
    
    return diccionario_pacientes

def dar_de_alta(lista_pacientes: list[dict]):
    """Da de alta al paciente validando sus datos

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
    """
    nombre = obtener_dato("Ingrese el nombre del paciente: ")
    apellido = obtener_dato("Ingrese el apellido del paciente: ")
    edad = get_int("Ingrese la edad del paciente: ", 1, 120)
    altura = get_int("Ingrese la altura del paciente: ", 30, 230)
    peso = get_float("Ingrese el peso del paciente: ", 10, 300)
    
    dni = get_int("Ingrese el DNI del paciente: ", 4000000, 99999999)
    validar_dni(dni) 
    
    grupo_sanguineo = obtener_grupo_sanguineo("Ingrese el grupo sanguineo del paciente: ")

    diccionario_pacientes = crear_paciente(nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
    lista_pacientes.append(diccionario_pacientes)

def modificar_paciente(lista_pacientes: list[dict], dni: int) -> str:
    """Modifica el o los datos de un paciente de la lista 

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
        dni (int): dni del paciente a modificar

    Returns:
        str: str si no se encuentra al empleado
    """
    paciente_encontrado = False
    
    for paciente in lista_pacientes:
        if paciente['dni'] == dni:
            paciente_encontrado = True
            print("Paciente encontrado")
            
            while True:
                opcion = input("1. Nombre\n2. Apellido\n3. Edad\n4. Altura\n5. Peso\n6. DNI\n7. Grupo sanguineo\n8. Salir de modificar\nElija una opcion: ")
                
                match opcion:
                    case "1":
                        nuevo_nombre = obtener_dato("Ingrese el nuevo nombre del paciente: ")
                        confirmar_modificacion(paciente, "nombre", nuevo_nombre)
                    case "2":
                        nuevo_apellido = obtener_dato("Ingrese el nuevo apellido del paciente: ")
                        confirmar_modificacion(paciente, "apellido", nuevo_apellido)
                    case "3":
                        nueva_edad = get_int("Ingrese la nueva edad del paciente: ", 1, 120)
                        confirmar_modificacion(paciente, "edad", nueva_edad)
                    case "4":
                        nueva_altura = get_int("Ingrese la nueva altura del paciente: ", 30, 230)
                        confirmar_modificacion(paciente, "altura", nueva_altura)
                    case "5":
                        nuevo_peso = get_float("Ingrese el nuevo peso del paciente: ", 10, 300)
                        confirmar_modificacion(paciente, "peso", nuevo_peso)
                    case "6":
                        nuevo_dni = get_int("Ingrese el nuevo DNI del paciente: ", 4000000, 99999999)
                        confirmar_modificacion(paciente, "dni", nuevo_dni)
                    case "7":
                        nuevo_grupo_sanguineo = obtener_grupo_sanguineo("Ingrese el nuevo grupo sanguineo del paciente: ")
                        confirmar_modificacion(paciente, "grupo sanguineo", nuevo_grupo_sanguineo)
                    case "8":
                        while True:
                            seguir_modificando = input("Esta seguro que no quiere modificar mas datos? si/no: ").lower()
                            if seguir_modificando == "si":
                                return
                            elif seguir_modificando == "no":
                                break
                            else:
                                print("Error, opcion invalida")
                    case _:
                        print("Error, el dato ingresado no es valido")
    
    if paciente_encontrado == False:
        print("Error, paciente no encontrado")

def eliminar_paciente(lista_pacientes: list[dict], dni: int):
    """Elimina permanentemente a un paciente de la lista

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
        dni (int): dni del paciente a eliminar
    """
    paciente_eliminado = None
    for paciente in lista_pacientes:
        if paciente['dni'] == dni:
            print("Paciente encontrado")
            paciente_eliminado = paciente
            break
        
    if paciente_eliminado != None:
        while True:
            desea_confirmar = input("Desea eliminar al paciente? si/no: ").lower()
            if desea_confirmar == "si":
                lista_pacientes.remove(paciente_eliminado)
                print("El paciente ha sido eliminado")
                break
            elif desea_confirmar == "no":
                print("El paciente no ha sido eliminado")
                break
            else:
                print("Error, opcion invalida")
    else:
        print("Error, paciente no encontrado")
        
def mostrar_todos(lista_pacientes: list[dict]):
    """Muestra todos los pacientes que han sido dados de alta

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
    """
    print("*"*108)
    print(f' |{"Nombre":^15} | {"Apellido":^15} | {"Edad":^10} | {"Altura":^10} | {"Peso":^10} | {"DNI":^10} | {"Grupo sanguineo":^15} |')
    print("-"*108)
    for i in range(len(lista_pacientes)):
        mostrar_un_paciente(lista_pacientes[i])
    print("*"*108)

def ordenar_pacientes(lista_pacientes: list[dict]):
    """Ordena los pacientes de forma ascendente o descendente segun el criterio

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
    """
    tipo_de_orden = get_string("1. Ascendente\n2. Descendente\nElija una opcion: ", 1)
    validar_tipo_de_orden(tipo_de_orden, "Error, ingrese una opcion valida: ")
    criterio_de_ordenamiento = None
    
    while True:
        opcion = input("A. Por nombre\nB. Por apellido\nC. Por altura\nD. Por grupo sanguineo\nElija una opcion: ").upper()
    
        match opcion:
            case "A":
                criterio_de_ordenamiento = "nombre"
                break
            case "B":
                criterio_de_ordenamiento = "apellido"
                break
            case "C":
                criterio_de_ordenamiento = "altura"
                break
            case "D":
                criterio_de_ordenamiento = "grupo sanguineo"
                break
            case _:
                print("Error, opcion invalida")
    
    ordenar_segun_tipo_de_orden(lista_pacientes, criterio_de_ordenamiento, tipo_de_orden)
        
    for paciente in lista_pacientes:
        print(paciente)

def buscar_paciente_por_dni(lista_pacientes: list[dict], dni: int) -> dict:
    """Busca a un paciente por su dni

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
        dni (int): dni del paciente a buscar

    Returns:
        dict: dict con la informacion del paciente si lo encuentra
    """
    for paciente in lista_pacientes:
        if paciente['dni'] == dni:
            mostrar_un_paciente(paciente)
            return paciente
    else:
        print("Error, paciente no encontrado")

def calcular_promedio(lista_pacientes: list[dict]) -> str :
    """Calcula el promedio segun criterio

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta

    Returns:
        str: str al calcular el promedio o si hay un error con la opcion ingresada
    """
    while True:
        opcion = input("A. Por edad\nB. Por altura\nC. Por peso\nD. Salir de promedio \nElija una opcion: ").upper() 
        
        match opcion:
            case "A":
                promedio_edad = promedio(lista_pacientes, "edad")
                return f"La edad promedio es: {promedio_edad}"
            case "B":
                promedio_altura = promedio(lista_pacientes, "altura")
                return f"La altura promedio es: {promedio_altura}"
            case "C":
                promedio_peso = promedio(lista_pacientes, "peso")
                return f"El peso promedio es: {promedio_peso}"
            case "D":
                calcular_otro_promedio = input("Esta seguro que no quiere calcular mas promedios? si/no: ").lower()
                if calcular_otro_promedio == "si":
                    break
            case _:
                print("Error, opcion invalida")

def determinar_compatibilidad(lista_pacientes: list[dict], dni: int):
    """Determina la compatibilidad de donantes

    Args:
        lista_pacientes (list[dict]): lista de pacientes dados de alta
        dni (int): dni del paciente
    """
    paciente = buscar_paciente_por_dni(lista_pacientes, dni)    
    
    grupo_sanguineo = paciente["grupo sanguineo"]
        
    puede_donarle_sangre_a = puede_donar[grupo_sanguineo]
    print(f"El paciente puede donarle sangre a: {puede_donarle_sangre_a}")
        
    puede_recibir_sangre_de = puede_recibir[grupo_sanguineo]
    print(f"El paciente puede recibir sangre de: {puede_recibir_sangre_de}")
    
    donantes_compatibles = es_donante_compatible(lista_pacientes, puede_recibir_sangre_de, dni)
    
    if donantes_compatibles:
        print(f"Los primeros 3 donantes compatibles con el paciente son: ")
        for donante in donantes_compatibles:
            print(f"{donante['nombre']} - {donante['apellido']} - {donante['dni']}")
    else:
        print("No existen donantes compatibles con el paciente")
        
def crear_matriz(lista_pacientes: list[dict]) -> list[list]:
    """Crea una matriz

    Args:
        lista_pacientes (list[dict]): lista de pacientes dados de alta

    Returns:
        list[list]: Matriz donde cada fila representa un tipo sanguineo
    """
    matriz = []
    for tipo_sanguineo in puede_donar:
        puede_donarle_sangre_a = 0
        puede_recibir_sangre_de = 0
        
        for paciente in lista_pacientes:
            if paciente["grupo sanguineo"] in puede_donar[tipo_sanguineo]:
                puede_donarle_sangre_a += 1

            if tipo_sanguineo in puede_donar[paciente["grupo sanguineo"]]:
                puede_recibir_sangre_de += 1
        
        matriz.append([tipo_sanguineo, puede_donarle_sangre_a, puede_recibir_sangre_de])
    
    return matriz

