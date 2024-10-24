import json
import os

path=os.path.dirname(os.path.abspath(__file__))
arch_div = os.path.join(path, f"Usuarios.json")
tablas=open(arch_div, "r")
contenido_tablas=json.load(tablas)
tablas.close()
tuplas_usuarios=[]
for usuario in contenido_tablas:
    puntaje=contenido_tablas[usuario]["puntaje"]
    tuplas_usuarios.append((puntaje,usuario))
print(tuplas_usuarios)
tuplas_o=tuple(sorted(tuplas_usuarios,reverse=True))
print(tuplas_o)