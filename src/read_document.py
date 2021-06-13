# esta funcion lee el archivo pokemon_data.csv y
def data_of_pokemons():
    read_file = open("pokemon_data.csv", "r")
    basic_information = []
    for leer_linea_por_linea in read_file:
        list_data = leer_linea_por_linea.replace('\n', "").split(sep=",")
        basic_information.append(list_data)
    read_file.close()
    return basic_information

# buscar la posicion de la lista de un nombre
def buscar_nombre(name: str, nombre_lista: list):
    posicion = False
    for x in range(832):
        if nombre_lista[x][0] == name.lower():
            posicion += x
            break
    return posicion


def mostrar_habilidades(posicion_pokemon: int, lista_pokemon: list):
    cortar = lista_pokemon[posicion_pokemon][8].split(sep=";")
    recorre = 0
    for recorrer in cortar:
        print(f"{recorre} - {recorrer}")
        recorre += 1



