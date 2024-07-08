def validate_number(numero: int|float, mensaje_error:str, minimo:int, maximo:int) -> int|float:
    """Valida si el numero esta dentro del minimo y maximo

    Args:
        numero (int|float): numero ingresado
        mensaje_error (str): mensaje de error si el numero esta fuera del rango permitido
        minimo (int): rango minimo permitido
        maximo (int): rango maximo permitido

    Returns:
        int|float: int|float si el numero esta dentro del rango
    """
    while numero < minimo or numero > maximo:
        numero = input(mensaje_error)
        numero = float(numero)
            
    return numero

def validate_length(cadena: str, mensaje_error:str, longitud:int) -> str:
    """Valida si la cadena tiene la longitud permitida

    Args:
        cadena (str): cadena ingresada
        mensaje_error (str): mensaje de error si la cadena esta fuera de la longitud permitida
        longitud (int): longitud maxima que puede tener la cadena
    Returns:
        str: str si la cadena tiene la longitud permitida
    """
    while len(cadena) > longitud:
        cadena = input(mensaje_error)
    
    return cadena

def validar_cadena(cadena: any, mensaje_error: str) -> str:
    """Valida si la cadena ingresada contiene solo caracteres alfabeticos

    Args:
        cadena (str): cadena ingresada
        mensaje_error (str): mensaje de error si la cadena no es alfabetica

    Returns:
        str: cadena capitalizada si es alfabetica
    """
    while not cadena.isalpha():
        cadena = input(mensaje_error)
    
    return cadena.capitalize()

def validar_dni(dni: int) -> int:
    """Valida si el dni tiene la cantidad de caracteres correctos

    Args:
        dni (int): dni del paciente

    Returns:
        int: Dni rellenado convertido a int nuevamente
    """
    dni = str(dni).split('.')[0]    
    if len(dni) < 8:
        dni = dni.zfill(8)
    
    return int(dni)
        
def validar_grupo_sanguineo(grupo_sanguineo: str, mensaje_error: str) -> str:
    """Valida el grupo sanguineo

    Args:
        grupo_sanguineo (str): grupo sanguineo ingresado
        mensaje_error (str): mensaje de error si lo ingresado no es valido

    Returns:
        str: str si lo ingresado es correcto
    """
    grupo_sanguineo = grupo_sanguineo.upper()
    grupos_sanguineos_posibles = ("A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-")
    while grupo_sanguineo not in grupos_sanguineos_posibles:
        grupo_sanguineo = input(mensaje_error)
        grupo_sanguineo = grupo_sanguineo.upper()
        
    return grupo_sanguineo

def validar_tipo_de_orden(tipo_de_orden: str, mensaje_error: str) -> str:
    """Valida el tipo de orden 

    Args:
        tipo_de_orden (str): tipo de orden ingresado
        mensaje_error (str): mensaje de error si lo ingresado no es valido

    Returns:
        str: str si lo ingresado es correcto
    """
    while tipo_de_orden != "1" and tipo_de_orden != "2":
        tipo_de_orden = input(mensaje_error)
    
    return tipo_de_orden