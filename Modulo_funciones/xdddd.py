barcosj1 = [[(1,1),(1,2),(1,3)], [(1,1),(1,2)], [], [], []]

def deteccion_hits(hit, lista_barcos):
    i = 0
    encontrado = False
    while i < len(lista_barcos) and encontrado == False:
        j = 0
        while j < len(lista_barcos[i]) and encontrado == False:
            if hit == lista_barcos[i][j] and encontrado == False:
                del lista_barcos[i][j]
                encontrado = True
                if not lista_barcos[i]:
                    del lista_barcos[i]
            j += 1
        i += 1

for i in range(3):
    x=int(input("x"))
    y=int(input("y"))
    pos_bomba=(x,y)
    deteccion_hits(pos_bomba, barcosj1)
    print(barcosj1)