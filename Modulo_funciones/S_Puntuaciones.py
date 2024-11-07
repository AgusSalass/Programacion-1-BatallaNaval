import json
import os


def leer_archivo():
	try:
		path_archivo = os.path.dirname(os.path.abspath(__file__))
		arch_dic = os.path.join(path_archivo, f"Usuarios.json")
		contenido = open(arch_dic,"r")
		cont_existente = contenido.read()
		contenido.close()
		diccionario_usuarios = json.loads(cont_existente)
		return diccionario_usuarios
	except TypeError:
		print(TypeError)
		print("Error de lectura")

usuarios = leer_archivo()
cuenta=("12345")
tuplas_usuarios=[]
print("\n\t\t\tTABLERO DE PUNTUACIONES")
print("\t\t\t-------------------------")

puntaje=usuarios[cuenta]["puntaje"]
tuplas_usuarios.append((puntaje,cuenta))
tuplas_o=sorted(tuplas_usuarios,reverse=True)
for puntaje,usuario in tuplas_o:
	print(f"\t\t\t{usuario}: {puntaje}")

