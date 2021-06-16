#Esta funcion lee un documento y luego todo lo que este con "\n y ," sera separado en una matriz
def matriz_de_lectura_de_documento(ruta: str):
    read_file = open(ruta, "r")
    basic_information = []
    for leer_linea_por_linea in read_file:
        listar_informacion = leer_linea_por_linea.replace('\n', "").split(sep=",")
        basic_information.append(listar_informacion)
    read_file.close()
    return basic_information


# buscar el punto donde esta posicionado el pokemon en la lista
def search_name(name: str, name_list: list, cantidad_datos: int):
    position = False
    for revisar_nombre in range(cantidad_datos):
        if name_list[revisar_nombre][0] == name.lower():
            position += revisar_nombre
            break
    return position


def mostrar_habilidad(posicion_pokemon: int, list_pokemon: list):
    cut = list_pokemon[posicion_pokemon][8].split(sep=";")
    recorre = 0
    for recorrer in cut:
        print(f"{recorre} - {recorrer}")
        recorre += 1


# buscara una habilidad en la lista genereda por la lectura del archivo
def buscar_habilidad_seleccionada(pokemon_position, posicion_habilidad: int, lista: list):
    cut = lista[pokemon_position][8].split(sep=";")
    return cut[posicion_habilidad]


# buscara el daño que le puede hacer un tipo de pokemon a otro tipo de pokemon
def analizar_efectividad(type_pokemon1: str, type_pokemon2: str, lista: list):
    posicion_tipo = search_name(type_pokemon1, lista, 19)
    buscar = lista[0].index(type_pokemon2)
    return float(lista[posicion_tipo][buscar])


def type_attack(type_pokemon, tipo_ataque):
    if type_pokemon == tipo_ataque:
        return 1.2
    else:
        return 1.0


def cantidad_habilidades(pokemon_position, lista: list):
    cut = lista[pokemon_position][8].split(sep=";")
    contar = 0
    for recorer in cut:
        contar += 1
    return contar - 1
