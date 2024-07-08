# Deberán crear una matriz que indique en la primera columna cada uno de los tipos
# sanguíneos, en la segunda a cuántas personas pueden donar y en la tercera de cuántas
# personas pueden recibir ese tipo, asegurarse que el desarrollo cuente con funciones
# minificadas y reutilizables. Realizar una función que reciba la matriz y la muestre.
from pacientes import *
from pacientes_secundarias import *

lista_pacientes = [
    {"Nombre": "Juan", "Apellido": "Pérez", "Edad": 35, "Altura": "170 cm", "Peso": "75 kg", "DNI": "12345678", "grupo sanguineo": "A+"},
    {"Nombre": "María", "Apellido": "Gómez", "Edad": 45, "Altura": "165 cm", "Peso": "60 kg", "DNI": "23456789", "grupo sanguineo": "B+"},
    {"Nombre": "Carlos", "Apellido": "Martínez", "Edad": 28, "Altura": "175 cm", "Peso": "80 kg", "DNI": "34567890", "grupo sanguineo": "0-"},
    {"Nombre": "Ana", "Apellido": "López", "Edad": 50, "Altura": "160 cm", "Peso": "70 kg", "DNI": "45678901", "grupo sanguineo": "AB+"},
    {"Nombre": "Pedro", "Apellido": "Sánchez", "Edad": 40, "Altura": "180 cm", "Peso": "85 kg", "DNI": "56789012", "grupo sanguineo": "A-"}
]

def crear_matriz(lista_pacientes: list[dict]):
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

def mostrar_matriz(matriz):
    print(f"{'TIpo':<3} {'Donar a':<3} {'Recibir de':<11}")
    for fila in matriz:
        print(f"{fila[0]:<3} {fila[1]:^8} {fila[2]:^11}")
