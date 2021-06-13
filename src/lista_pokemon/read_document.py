# esta funcion lee un documento y luego todo lo que este con "\n y ," sera separado en una matriz
def matriz_de_lectura_de_documento(ruta: str):
    read_file = open(ruta, "r")
    basic_information = []
    for leer_linea_por_linea in read_file:
        list_data = leer_linea_por_linea.replace('\n', "").split(sep=",")
        basic_information.append(list_data)
    read_file.close()
    return basic_information


# buscar la posicion en la lista donde esta posicionado un pokemon nombre
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


# buscara una habilidad en la lista genereda por la lectura del archivo
def buscar_habilidad_seleccionada(posicion_pokemon, posicion_habilidad: int, lista: list):
    cortar = lista[posicion_pokemon][8].split(sep=";")
    return cortar[posicion_habilidad]
