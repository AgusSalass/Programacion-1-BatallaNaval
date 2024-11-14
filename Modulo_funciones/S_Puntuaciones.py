import json
import os
import re

def obtener_puntaje(usuario):
    try:
        path_archivo = os.path.dirname(os.path.abspath(__file__))
        arch_dic = os.path.join(path_archivo, f"Usuarios.json")
        contenido = open(arch_dic,"r")
        cont_existente = contenido.read()
        contenido.close()
        diccionario_usuarios = json.loads(cont_existente)
        puntaje = diccionario_usuarios[usuario]["puntaje"]
        return puntaje
    except TypeError:
        print(TypeError)
        print("Error de lectura")

def leer_archivo(tipo_archivo):
	try:
		path_archivo = os.path.dirname(os.path.abspath(__file__))
		arch_dic = os.path.join(path_archivo, tipo_archivo)
		contenido = open(arch_dic,"r")
		cont_existente = contenido.read()
		contenido.close()
		diccionario = json.loads(cont_existente)
		return diccionario
	except TypeError:
		print(TypeError)
		print("Error de lectura")

def grabar_scoreboard(puntaje, diccionario_scoreboard):
    alias = str(input("Ingrese un alias (3 Caracteres, solo letras): "))
    while not re.match("^[A-Z]{3}$", alias):
        os.system("cls")
        print("Alias invalido")
        alias = str(input("Ingrese un alias (3 Caracteres, solo letras): "))
        
    diccionario_scoreboard[alias] = {
        "puntaje": puntaje
    }
    scoreboard_JSON = json.dumps(diccionario_scoreboard, indent=4)
    try:
        path_archivo = os.path.dirname(os.path.abspath(__file__))
        arch_dic = os.path.join(path_archivo, f"Scoreboard.json")
        contenido = open(arch_dic, "w")
        contenido.write(scoreboard_JSON)
        contenido.close()
    except TypeError:
        print(TypeError)
        print("Error de grabado")

def imprimir_scoreboard(diccionario_scoreboard):
     tuplas_usuarios = []
     print("\n\t\t\tTABLERO DE PUNTUACIONES")
     print("\t\t\t-------------------------")
     for usuario, puntos in diccionario_scoreboard.items():
        puntaje = puntos["puntaje"]
        tuplas_usuarios.append((puntaje, usuario))
        tuplas_usuarios = sorted(tuplas_usuarios, reverse = True)
     for puntaje, usuario in tuplas_usuarios[:10]:
        print(f"\t\t\t{usuario}: {puntaje}")

#programa principal
tuplas_usuarios = []
cuenta = "12345"
archivo = "Scoreboard.json"
puntos_cuenta = obtener_puntaje(cuenta)
scoreboard = leer_archivo(archivo)
grabar_scoreboard(puntos_cuenta, scoreboard)
scoreboard = leer_archivo(archivo)
imprimir_scoreboard(scoreboard)