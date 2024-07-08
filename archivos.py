import re
def crear_archivo(path: str, lista_pacientes: list[dict]):
    """Crea y escribe el archivo con los datos de la lista de pacientes

    Args:
        path (str): ruta del archivo a crear
        lista_pacientes (list[dict]): lista de pacientes dados de alta
    """
    try:
        with open(path, "w", encoding = "utf8") as archivo:
            archivo.write(f"nombre, apellido, edad, altura, peso, dni, grupo sanguineo \n ")
            for paciente in lista_pacientes:
                linea = (f" {paciente['nombre']},{paciente['apellido']}, {paciente['edad']}, {paciente['altura']}, {paciente['peso']}, {paciente['dni']}, {paciente['grupo sanguineo']} \n ")
                archivo.write(linea)
        
        print("Archivo creado correctamente")
        
    except:
        print("Error, no fue posible crear el archivo")

def lectura_archivo(path: str) -> list:
    """Lee un archivo de pacientes y devuelve una lista de diccionarios con los datos

    Args:
        path (str): ruta del archivo

    Returns:
        list: lista de diccionarios, cada diccionario representa a un paciente
    """
    lista_pacientes = []
    try:
        bandera_pasar_linea = False
        with open(path, "r", encoding = "utf8") as archivo:
            for linea in archivo:
                if bandera_pasar_linea == False:
                    bandera_pasar_linea = True
                    continue #se crea una bandera para que saltee la 1er fila que contiene los "titulos"
                registro_paciente = re.split(",|\n", linea)
                diccionario_pacientes = {}
                diccionario_pacientes["nombre"] = registro_paciente[0]
                diccionario_pacientes["apellido"] = registro_paciente[1]
                diccionario_pacientes["edad"] = registro_paciente[2]
                diccionario_pacientes["altura"] = registro_paciente[3]
                diccionario_pacientes["peso"] = registro_paciente[4]
                diccionario_pacientes["dni"] = registro_paciente[5]
                diccionario_pacientes["grupo sanguineo"] = registro_paciente[6]
                
                lista_pacientes.append(diccionario_pacientes)            
    
    except:
        print("Error, archivo no encontrado")
    
    return lista_pacientes 

def guardar_archivo(path: str, lista_pacientes: list[dict]):
    """Guarda los cambios en el archivo CSV

    Args:
        path (str): ruta del archivo
        lista_pacientes (list[dict]): lista de pacientes dados de alta
    """
    try:
        with open(path, "w", encoding = "utf8") as archivo:
            archivo.write(f"nombre, apellido, edad, altura, peso, dni, grupo sanguineo \n ")
            for paciente in lista_pacientes:
                linea = (f" {paciente['nombre']},{paciente['apellido']}, {paciente['edad']}, {paciente['altura']}, {paciente['peso']}, {paciente['dni']}, {paciente['grupo sanguineo']} \n ")
                archivo.write(linea)
            
        print("Cambios guardados en el archivo")
    
    except:
        print("Error, archivo no encontrado")


