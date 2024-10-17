barcosj1 = [[(1,1),(1,2),(1,3),(1,4),(1,5)],[(1,1),(1,2),(1,3),(1,4)],[(1,1),(1,2),(1,3)],[(1,1),(1,2),(1,3)],[(1,1),(1,2)]]

o = (f"\033[36m ~\033[0m")
b = (f"\033[90m ≡\033[0m")
portaaviones = b
mulportaaviones = 5
destructor = b
muldestructor = 4
crucero1 = b
mulcrucero1= 3
crucero2 = b
mulcrucero2 = 3
lancha = b
mullancha = 2

j1_tablerodisparos= [["╔","══","══","══","══","══","══","══","══","══","══","═╗","portaaviones: ",portaaviones*mulportaaviones],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║","destructor: ",destructor*muldestructor],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║","crucero: ",crucero1*mulcrucero1],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║","crucero: ",crucero2*mulcrucero2],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║","lancha: ", lancha*mullancha],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                        ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                        ["╠","══","══","══","══","══","══","══","══","══","══","═╣"]]

def deteccion_hits(hit, lista_barcos, tablero, xportaaviones, xdestructor, xcrucero1, xcrucero2, xlancha):
    i = 0
    encontrado = False
    while i < len(lista_barcos) and encontrado == False:
        j = 0
        while j < len(lista_barcos[i]) and encontrado == False:
            if hit == lista_barcos[i][j] and encontrado == False:
                del lista_barcos[i][j]
                encontrado = True
                if lista_barcos[i] == []:
                    #hardcodeado, ver como evitar
                    if i == 0:
                        tablero[i][13] = (f"\033[31mDestruido\033[0m")
                        xportaaviones = 1
                    elif i == 1:
                        tablero[i][13] = (f"\033[31mDestruido\033[0m")
                        xdestructor = 1
                    elif i == 2:
                        tablero[i][13] = (f"\033[31mDestruido\033[0m")
                        xcrucero1 = 1
                    elif i == 3:
                        tablero[i][13] = ( f"\033[31mDestruido\033[0m")
                        xcrucero2 = 1
                    elif i == 4:
                        tablero[i][13] = (f"\033[31mDestruido\033[0m")
                        xlancha = 1
            j += 1
        i += 1
    return xportaaviones, xdestructor, xcrucero1, xcrucero2, xlancha

def dibujar(tablero):
    for fila in tablero:
        for columna in fila:
            print(columna,end="")
        print()

while True:
    x=int(input("x"))
    y=int(input("y"))
    pos_bomba=(x,y)
    mulportaaviones, muldestructor, mulcrucero1, mulcrucero2, mullancha = deteccion_hits(pos_bomba, barcosj1, j1_tablerodisparos, mulportaaviones, muldestructor, mulcrucero1, mulcrucero2, mullancha)
    print(barcosj1)
    dibujar(j1_tablerodisparos)