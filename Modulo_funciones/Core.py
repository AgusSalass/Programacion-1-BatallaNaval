import os

def mostrar_equipo():
    print("Este es nuestro equipo")
    for i in Equipo:
        print(i)


def mostrar_proyecto():
    print("Nuestro proyecto se trata sobre el juego de mesa Batalla Naval") #TODO revisar esta funcion

#menu
def menu():

    repetir = True
    while  repetir:
        os.system("cls")
        print ("1-Equipo")
        print ("2-Proyecto")
        print ("4-Salir")
        try:
            op=int(input("Eliga una opcion: "))
            
            if op==1:
                mostrar_equipo()
            elif op==2:
                mostrar_proyecto()
            elif op==4:
                repetir=False
            else:
                print("Opcion invalida")
            input()
        except:
            print("Error, debe usar un numero")
            input()
            
Equipo = ["Diaz, German Ezequiel", "Nuñez, Francisco", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella", "Trimarco, Tomas"]


#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir