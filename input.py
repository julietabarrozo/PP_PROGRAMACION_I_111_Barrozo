from validate import *
def get_int(mensaje:str, minimo: int, maximo: int) -> int:
    """Solicita el ingreso de un int

    Args:
        mensaje (str): mensaje para solicitar el ingreso
        minimo (int): rango minimo permitido
        maximo (int): rango maximo permitido

    Returns:
        int: int si el numero esta dentro del rango
    """
    while True:
        numero = input(mensaje)
        if numero.isnumeric():
            numero = int(numero)    
            resultado = validate_number(numero, "Error, ingrese nuevamente: ", minimo, maximo)
            return resultado
        else:
            print("Error, debe ingresar un numero entero")  

def get_float(mensaje:str, minimo: int, maximo: int) -> float:
    """Solicita el ingreso de un float

    Args:
        mensaje (str): mensaje para solicitar el ingreso
        minimo (int): rango minimo permitido
        maximo (int): rango maximo permitido

    Returns:
        float: float si el numero esta dentro del rango
    """
    while True:
        numero = input(mensaje)
        if es_float(numero):
            numero = float(numero)
                
            resultado = validate_number(numero, "Error, ingrese nuevamente: ", minimo, maximo)

            return resultado
        else:
            print("Error, debe ingresar un numero flotante")

def es_float(valor: str) -> bool:
    """Verifica si un string puede convertirse a float

    Args:
        valor (str): cadena a verificar

    Returns:
        bool: True si el valor puede convertirse a float, False en caso contrario
    """
    try:
        float(valor)
        return True
    except ValueError:
        return False

def get_string(mensaje:str, longitud: int) -> str:
    """Solicita el ingreso de una cadena

    Args:
        mensaje (str): mensaje para solicitar el ingreso
        longitud (int): longitud maxima que puede tener la cadena

    Returns:
        str: str si la cadena tiene la longitud permitida
    """
    cadena = input(mensaje)
    
    resultado = validate_length(cadena, "Error, ingrese nuevamente: ", longitud)
    
    return resultado

def obtener_dato(mensaje: str) -> str:
    """Obtiene un dato 

    Args:
        mensaje (str): mensaje para solicitar el dato

    Returns:
        str: cadena validada y capitalizada
    """
    dato = get_string(mensaje, 20)
    resultado = validar_cadena(dato, "Error, ingrese nuevamente: ")
    
    return resultado

def obtener_grupo_sanguineo(mensaje: str) -> str:
    """Obtiene el grupo sanguineo

    Args:
        mensaje (str): mensaje para solicitar el grupo sanguineo

    Returns:
        str: cadena validada
    """
    grupo_sanguineo = get_string(mensaje, 3)
    grupo_sanguineo.upper()
    resultado = validar_grupo_sanguineo(grupo_sanguineo, "Error, ingrese nuevamente: ")
    
    return resultado