j1_barcos = [[(0,0),(0,1),(0,2)],[(1,0),(2,0),(3,0),]]
hit = (0,0)
i = 0
encontrado = False
while i < len(j1_barcos) and encontrado == False:
    j = 0
    while j < len(j1_barcos[i]) and encontrado == False:
        if hit == j1_barcos[i][j] and encontrado == False:
            del j1_barcos[i][j]
            encontrado = True
            if j1_barcos[i] == []:
                del j1_barcos[i]
                print("barco hundido")
        j += 1
    i += 1
print(j1_barcos)

