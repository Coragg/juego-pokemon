# esta funcion lee un documento y luego todo lo que este con "\n y ," sera separado en una matriz
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
def buscar_habilidad_seleccionada(posicion_pokemon, posicion_habilidad: int, lista: list):
    cut = lista[posicion_pokemon][8].split(sep=";")
    return cut[posicion_habilidad]


#
def analizar_efectividad(tipo_pokemon1: str, tipo_pokemon2: str, lista: list):
    posicion_tipo = search_name(tipo_pokemon1, lista, 19)
    buscar = lista[0].index(tipo_pokemon2)
    return lista[posicion_tipo][buscar]

# data = matriz_de_lectura_de_documento("tabla_efectividad.csv")
# dd = analizar_efectividad("bug", "rock", data)
# print(type(dd))


def type_attack(tipo_pokemon, tipo_ataque):
    if tipo_pokemon == tipo_ataque:
        return 1.2
    else:
        return 1.0






