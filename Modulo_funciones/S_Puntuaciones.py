import re
import json
import os


path=os.path.dirname(os.path.abspath(__file__))
arch_div = os.path.join(path, f"Usuarios.json")
tablas=open(arch_div, "r")
contenido_tablas=json.load(tablas)
print(contenido_tablas)
tablas.close()

