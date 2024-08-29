import os

#menu
def menu():
    repetir = True
    while  repetir:
        os.system("cls")
        print ("1-Equipo")
        print ("2-Instrucciones")
        print ("3-Ejecutar")
        print ("4-Salir")
        try:
            op=int(input("Eliga una opcion: "))
            
            if op==1:
                mostrar_equipo()
            elif op==2:
                mostrar_instrucciones()
            elif op==3:
                ejecutar()
            elif op==4:
                repetir=False
            else:
                print("Opcion invalida")
            input()
        except:
            print("Error")
            input()
            
            
#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir