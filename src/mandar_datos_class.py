from datos_pokemo import caracteristicas_pokemon as send

def send_data(lista: list, ruta, object):
    object = send.CaracteristicasPokemon()
    object.set_name(lista[ruta][0])
    object.set_type_pokemon(lista[ruta][1])
    object.set_hp(lista[ruta][2])
    object.set_attack(lista[ruta][3])
    object.set_defense(lista[ruta][4])
    object.set_special_attack(lista[ruta][5])
    object.set_special_defense(lista[ruta][6])
    object.set_velocity(lista[ruta][7])
