# leer el archivo y nos genera una lista con todos los datos separados en forma de matriz
def leer_efectividad():
    read_file = open("tabla_efectividad.csv", "r")
    tabla_efectividad = []
    for leer_linea_por_linea in read_file:
        list_data = leer_linea_por_linea.replace('\n', "").split(sep=",")
        tabla_efectividad.append(list_data)
    read_file.close()
    return tabla_efectividad
