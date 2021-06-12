read_file = open("pokemon_data.csv", "r")


# datos separados por salto de linea
informacion_salto_linea = []
for leer_linea_por_linea in read_file:
    listar_data = leer_linea_por_linea.replace('\n', "").split(sep=",")
    informacion_salto_linea.append(listar_data)

# print(informacion_salto_linea[0])
name_attack = ""

print(type(informacion_salto_linea[0][8]))
cortar = informacion_salto_linea[0][8].split(sep=";")
print(cortar)
for recorer in cortar:
    print(recorer)


read_file.close()
