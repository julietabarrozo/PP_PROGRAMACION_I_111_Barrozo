from archivos import *

#funciones secundarias del codigo
def asignar_id(lista_ids: list) -> int :
    """Asigna un id a un empleado

    Args:
        lista_ids (list): lista de ids que acumula los ids que ya fueron asignados

    Returns:
        int: int que es el id del nuevo paciente dado de alta
    """
    if len(lista_ids) == 0:
        id_nuevo_paciente = 1
    else:
        ultimo_id_asignado = lista_ids.pop()
        id_nuevo_paciente = ultimo_id_asignado + 1
        lista_ids.append(ultimo_id_asignado)
    lista_ids.append(id_nuevo_paciente)
    return id_nuevo_paciente

def confirmar_modificacion(paciente: dict, dato: str, nuevo_dato: str|int|float):
    """Confirma la modificacion del dato de un paciente

    Args:
        paciente (dict): paciente a modificar
        dato (str): dato a modificar
        nuevo_dato (str | int | float): dato modificado
    """
    while True:
        desea_confirmar = input("Desea modificar? si/no: ").lower()
        if desea_confirmar == "si":
            paciente[dato] = nuevo_dato
            print(f"El {dato} del paciente ha sido modifcado")
            break
        elif desea_confirmar == "no":
            print(f"El {dato} del paciente no ha sido modificado")
            break
        else:
            print("Error, opcion invalida")

def mostrar_un_paciente(paciente: dict):
    """Muestra los datos de un paciente

    Args:
        paciente (dict): paciente a mostrar
    """
    print(f' |{paciente["nombre"]:^15} | {paciente["apellido"]:^15} | {paciente["edad"]:^10} | {paciente["altura"]:>8}cm | {paciente["peso"]:>8}kg | {paciente["dni"]:^10} | {paciente["grupo sanguineo"]:^15} |')

def ordenar_segun_tipo_de_orden(lista_pacientes: list[dict], criterio_de_ordenamiento: str, tipo_de_orden: str):
    """Ordena la lista de pacientes según criterio de ordenamiento y tipo de orden especificado.

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
        criterio_de_ordenamiento (str): clave del diccionario para ordenar
        tipo_de_orden (str): tipo de orden para ordenar
    """
    for i in range ((len(lista_pacientes)) - 1):
        for j in range (0, (len(lista_pacientes)) - i - 1): #determina cuántos elementos hay que considerar en cada iteración de i, ya que los últimos i elementos ya están ordenados.
            if tipo_de_orden == "1":
                if lista_pacientes[j][criterio_de_ordenamiento] > lista_pacientes[j + 1][criterio_de_ordenamiento]: #j + 1 para acceder al siguiente elemento y compararlo con el elemento actual
                    variable_temporal = lista_pacientes[j]
                    lista_pacientes[j] = lista_pacientes[j + 1]
                    lista_pacientes[j + 1] = variable_temporal
            
            elif tipo_de_orden == "2":
                if lista_pacientes[j][criterio_de_ordenamiento] < lista_pacientes[j + 1][criterio_de_ordenamiento]:
                    variable_temporal = lista_pacientes[j]
                    lista_pacientes[j] = lista_pacientes[j + 1]
                    lista_pacientes[j + 1] = variable_temporal
                    
def promedio(lista_pacientes: list[dict], dato: str) -> float:
    """Calcula el promedio de un dato especifico de la lista de pacientes

    Args:
        lista_pacientes (list[dict]): lista de diccionarios de pacientes dados de alta
        dato (str): dato del paciente

    Returns:
        float: float al calcular el promedio
    """
    acumulador = 0
    for paciente in lista_pacientes:
        acumulador += paciente[dato]
    promedio = (acumulador / len(lista_pacientes))
    
    return promedio

puede_donar = {'A+': ["A+","AB+"],
               'A-': ["A+","A-","AB+","AB-"],
               'B+': ["B+","AB+"],
               'B-': ["B+","B-","AB+","AB-"],
               'AB+': ["AB+","AB-"],
               'AB-': ["AB+","AB-"],
               '0+': ["A+","B+","AB+","0+"],
               '0-': ["A+","A-","AB+","AB-","B+","B-","0+","0-"]
               }

puede_recibir = {'A+': ["0+","0-","A+","A-"],
               'A-': ["0-","A-"],
               'B+': ["0+","0-","B+","B-"],
               'B-': ["0-","B-"],
               'AB+': ["A+","A-","AB+","AB-","B+","B-","0+","0-"],
               'AB-': ["AB-","0-","A-","B-"],
               '0+': ["0+","0-"],
               '0-': ["0-"]}

def es_donante_compatible(lista_pacientes: list[dict], puede_recibir_sangre_de: list, dni: int) -> list[dict]:
    """Valida si el donante es compatible con el paciente

    Args:
        lista_pacientes (list[dict]): lista de pacientes dados de alta
        puede_recibir_sangre_de (list): lista de grupos sanguineos 
        dni (int): dni del paciente
    
    Returns:
        list[dict]: lista de donantes compatibles
    """
    donantes_compatibles = []
    
    for paciente in lista_pacientes: 
        if paciente["dni"] != dni and paciente["grupo sanguineo"] in puede_recibir_sangre_de:
            donantes_compatibles.append(paciente)
    
    return donantes_compatibles[:3] #:3 indica que extrae lo que haya en la lista en los primeros 3 indices (0, 1, 2)

def mostrar_matriz(matriz):
    print(f"{'TIpo':<3} {'Donar a':<3} {'Recibir de':<11}")
    for fila in matriz:
        print(f"{fila[0]:<3} {fila[1]:^8} {fila[2]:^11}")
        
def confirmar_salida(lista_pacientes: list[dict]) -> bool:
    """Solicita al usuario confirmar si desea salir del menu de opciones

    Args:
        lista_pacientes (list[dict]): lista de pacientes dados de alta

    Returns:
        bool: True si el usuario confirma salir (y guarda los cambios en el archivo), False si el usuario decide no salir
    """
    while True:
        seguir = input("Esta seguro que quiere salir del menu? si/no: ").lower()
        if seguir == "si":
            guardar_archivo("Pacientes.csv", lista_pacientes)
            return True
        elif seguir == "no":
            return False
        else:
            print("Error, opcion invalida")        

