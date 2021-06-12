


# esta funcion lee el archivo pokemon_data.csv y
def data_of_pokemons():
    read_file = open("pokemon_data.csv", "r")
    basic_information = []
    for leer_linea_por_linea in read_file:
        list_data = leer_linea_por_linea.replace('\n', "").split(sep=",")
        basic_information.append(list_data)
    read_file.close()
    return basic_information
# print(informacion_salto_linea[0])


# print(data_of_pokemons())
informacion = data_of_pokemons()
# print(type(informacion[0][8]))


print(informacion[1][0])
cortar = informacion[1][8].split(sep=";")
print(cortar)
for recorer in cortar:
    print(recorer)



