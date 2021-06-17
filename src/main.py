# TDFI102.202110.10459.TR
# Trabajo Pokemon
# Integrantes: Anibal Muñoz (21087122-5), Victor Camero (25833773-5) y Sofia Castro (21042213-7).

from datos_pokemo import caracteristicas_pokemon as info_poke
from lista_pokemon import read_document as leer
from datos_pokemo import estadisticas
from movimiento import moves
import random

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
      ":::::::::::::::::::::::::::::::::::::")
print("::Bienvenido al simulador de combate pokemon profesional, aquí podra probar los daños que llegaria a hacer un "
      "pokemon profesional a otro           ::")
print("::Lo que debe hacer joven entrenador es: Elegir un pokemon de primera a septima generacion, el simulador te "
      "mostrara sus estadisisticas            ::")
print("::Despues tendras que elegir una habilidad que puede usar ese pokemon, despues te mostrara las estadisticas de "
      "un pokemon de categoria profesional ::")
print("::Acto seguido eligiras un pokemon para que reciba el ataque, el cual va a mostrar su estadistica de vida en "
      "modo profesional, tu pokemon          ::")
print("::Atacara al otro mostrando el daño que harian teoricamente 2 pokemones profesionales en una lucha real         "
      "                                   ::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
      ":::::::::::::::::::::::::::::::::::::")
print("::Reglas profecionales: Pokeones a nivel 50, IV=31 en cada estadistica, Ev=250 Total en estadisticas, "
      "dependiendo la temporada                     ::")
print("::Se permiten el uso de pokemones legendarios, pero si miticos y singularares.                                  "
      "             Disfrute el simulador ::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
      ":::::::::::::::::::::::::::::::::::::")

ruta_pokemon_data = "./lista_pokemon/pokemon_data.csv"
data_pokemon = leer.matriz_de_lectura_de_documento(ruta_pokemon_data)
ruta_tabla_efectividad = "./lista_pokemon/tabla_efectividad.csv"
tabla_efectivida = leer.matriz_de_lectura_de_documento(ruta_tabla_efectividad)
falso = False

# Recolectar informacion del primer pokemon
search_pokemon = False
while search_pokemon == falso:
    nombre_primer_pokemon = input("Elija su pokemon: ")
    search_pokemon = leer.search_name(nombre_primer_pokemon, data_pokemon, 832)

primer_pokemon = info_poke.CaracteristicasPokemon()
primer_pokemon.send_data(data_pokemon, search_pokemon)
print(f"Nombre del Pokémon seleccionado:  {primer_pokemon.get_name()}")
print("Estadisticas bases del pokémon: ")
print("\thp =", primer_pokemon.get_hp())
print("\tAtaque =", primer_pokemon.get_attack())
print("\tDefensa = ", primer_pokemon.get_defense())
print("\tAtaque especial =", primer_pokemon.get_special_attack())
print("\tDefensa especial =", primer_pokemon.get_special_defense())
print("\tVelociodad =", primer_pokemon.get_velocity())

print("\nMovimientos que puede aprender el pokémon: ")
leer.mostrar_habilidad(search_pokemon, data_pokemon)


seleccionar_ataque = int(input("Seleccione un ataque a ejecutar: "))
cantidad_habilidades = leer.cantidad_habilidades(search_pokemon, data_pokemon)
while seleccionar_ataque <= -1 or seleccionar_ataque > cantidad_habilidades:
    seleccionar_ataque = int(input("Seleccione un ataque a ejecutar: "))
nombre_hablidad_elegida = leer.buscar_habilidad_seleccionada(search_pokemon, seleccionar_ataque, data_pokemon)
informacion_hablidada = moves.get_move(nombre_hablidad_elegida)



print(f"El ataque seleccionado es:  {nombre_hablidad_elegida}")

amplified_life = estadisticas.health_point(int(primer_pokemon.get_hp()))
primer_pokemon.set_hp(amplified_life)
print(f"El hp al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_hp()}")
amplified_attack = estadisticas.other_stat(int(primer_pokemon.get_attack()))
primer_pokemon.set_attack(amplified_attack)
print(f"El atk al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_attack()}")
amplified_defense = estadisticas.other_stat(int(primer_pokemon.get_defense()))
primer_pokemon.set_defense(amplified_defense)
print(f"El def al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_defense()}")
amplified_special_attack = estadisticas.other_stat(int(primer_pokemon.get_special_attack()))
primer_pokemon.set_special_attack(amplified_special_attack)
print(f"El spa al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es "
      f"{primer_pokemon.get_special_attack()}")
amplified_special_defense = estadisticas.other_stat(int(primer_pokemon.get_special_defense()))
primer_pokemon.set_special_defense(amplified_special_defense)
print(f"El spd al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es "
      f"{primer_pokemon.get_special_defense()}")
amplified_velocity = estadisticas.other_stat(int(primer_pokemon.get_velocity()))
primer_pokemon.set_velocity(amplified_velocity)
print(f"El spe al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_velocity()}")

# Pokemon a enfrentar
segundo_poke = input("Ingrese el nombre del Pokémon a atacar: ")
search_second_pokemon = leer.search_name(segundo_poke, data_pokemon, 832)
while search_second_pokemon == falso:
    segundo_poke = input("Ingrese el nombre del Pokémon a atacar: ")
    search_second_pokemon = leer.search_name(segundo_poke, data_pokemon, 832)

segundo_pokemon = info_poke.CaracteristicasPokemon()
segundo_pokemon.send_data(data_pokemon, search_second_pokemon)
print(f"Nombre del Pokémon seleccionado: {segundo_pokemon.get_name()}")

amplified_hp = estadisticas.health_point(int(segundo_pokemon.get_hp()))
segundo_pokemon.set_hp(amplified_hp)
attack_amplified = estadisticas.other_stat(int(segundo_pokemon.get_attack()))
segundo_pokemon.set_attack(attack_amplified)
defense_amplified = estadisticas.other_stat(int(segundo_pokemon.get_defense()))
segundo_pokemon.set_defense(defense_amplified)
special_attack_amplified = estadisticas.other_stat(int(segundo_pokemon.get_special_attack()))
segundo_pokemon.set_special_attack(special_attack_amplified)
special_defense_amplified = estadisticas.other_stat(int(segundo_pokemon.get_special_defense()))
segundo_pokemon.set_special_defense(special_defense_amplified)
velocity_amplified = estadisticas.other_stat(int(segundo_pokemon.get_velocity()))
segundo_pokemon.set_velocity(velocity_amplified)


cantidad_habilidades_aleatorio = leer.cantidad_habilidades(search_second_pokemon, data_pokemon)
random_select = random.randrange(0, cantidad_habilidades_aleatorio)
name_hability_segundo_pokemon = leer.buscar_habilidad_seleccionada(search_second_pokemon, random_select, data_pokemon)

habilidad_segundo_pokemon = moves.get_move(name_hability_segundo_pokemon)


print(f"El hp al nivel {segundo_pokemon.get_level()} de {segundo_pokemon.get_name()} es {segundo_pokemon.get_hp()}")
power_primer_pokemon = informacion_hablidada[1]
power_segundo_pokemon = habilidad_segundo_pokemon[1]

# tercer prototipo de combate

while primer_pokemon.get_hp() > 0 and segundo_pokemon.get_hp() > 0:
    if primer_pokemon.get_velocity() > segundo_pokemon.get_velocity():
        # daño al segundo pokemon
        tipo_primer_pokemon = leer.analizar_efectividad(primer_pokemon.get_type_pokemon(),
                                                        segundo_pokemon.get_type_pokemon(),
                                                        tabla_efectivida)
        stab_primer_pokemon = leer.type_attack(primer_pokemon.get_type_pokemon(), informacion_hablidada[2])
        atacar_segundo_pokemon = estadisticas.damages(power_primer_pokemon, tipo_primer_pokemon, stab_primer_pokemon,
                                                      primer_pokemon.get_attack(),
                                                      segundo_pokemon.get_defense())
        segundo_pokemon.set_damages_received(atacar_segundo_pokemon)
        if segundo_pokemon.get_hp() > 0:
            print(f"El daño que realizó  {primer_pokemon.get_name()} a {segundo_pokemon.get_name()} fue de: "
                  f"{atacar_segundo_pokemon}")
            print(f"{segundo_pokemon.get_name()} quedó con un hp de: {segundo_pokemon.get_hp()}")
        else:
            print(f"Perdio {segundo_pokemon.get_name()}")
            break
        # daño al primer pokemon
        tipo_segundo_pokemon = leer.analizar_efectividad(segundo_pokemon.get_type_pokemon(),
                                                         primer_pokemon.get_type_pokemon(),
                                                         tabla_efectivida)
        stab_segundo_pokemon = leer.type_attack(segundo_pokemon.get_type_pokemon(), habilidad_segundo_pokemon[2])
        atacar_primer_pokemon = estadisticas.damages(power_segundo_pokemon, tipo_segundo_pokemon,
                                                     stab_segundo_pokemon, segundo_pokemon.get_attack(),
                                                     primer_pokemon.get_defense())
        primer_pokemon.set_damages_received(atacar_primer_pokemon)
        if primer_pokemon.get_hp() > 0:
            print(f"El daño que realizó  {segundo_pokemon.get_name()} a {primer_pokemon.get_name()} fue de: "
                  f"{atacar_primer_pokemon}")
            print(f"{primer_pokemon.get_name()} quedó con un hp de: {primer_pokemon.get_hp()}")
        else:
            print(f"Perdio {primer_pokemon.get_name()}")
            break
    else:
        # daño al primer pokemon
        tipo_segundo_pokemon = leer.analizar_efectividad(segundo_pokemon.get_type_pokemon(),
                                                         primer_pokemon.get_type_pokemon(),
                                                         tabla_efectivida)
        stab_segundo_pokemon = leer.type_attack(segundo_pokemon.get_type_pokemon(), habilidad_segundo_pokemon[2])
        atacar_primer_pokemon = estadisticas.damages(power_segundo_pokemon, tipo_segundo_pokemon,
                                                     stab_segundo_pokemon, segundo_pokemon.get_attack(),
                                                     primer_pokemon.get_defense())
        primer_pokemon.set_damages_received(atacar_primer_pokemon)
        if primer_pokemon.get_hp() > 0:
            print(f"El daño que realizó  {segundo_pokemon.get_name()} a {primer_pokemon.get_name()} fue de: "
                  f"{atacar_primer_pokemon}")
            print(f"{primer_pokemon.get_name()} quedó con un hp de: {primer_pokemon.get_hp()}")
        else:
            print(f"Perdio {primer_pokemon.get_name()}")
            break

        # daño al segundo pokemon
        tipo_primer_pokemon = leer.analizar_efectividad(primer_pokemon.get_type_pokemon(),
                                                        segundo_pokemon.get_type_pokemon(),
                                                        tabla_efectivida)
        stab_primer_pokemon = leer.type_attack(primer_pokemon.get_type_pokemon(), informacion_hablidada[2])
        atacar_segundo_pokemon = estadisticas.damages(power_primer_pokemon,
                                                      tipo_primer_pokemon, stab_primer_pokemon,
                                                      primer_pokemon.get_attack(),
                                                      segundo_pokemon.get_defense())
        segundo_pokemon.set_damages_received(atacar_segundo_pokemon)
        if segundo_pokemon.get_hp() > 0:
            print(f"El daño que realizó  {primer_pokemon.get_name()} a {segundo_pokemon.get_name()} fue de: "
                  f"{atacar_segundo_pokemon}")

            print(f"{segundo_pokemon.get_name()} quedó con un hp de: {segundo_pokemon.get_hp()}")
        else:
            print(f"Perdio {segundo_pokemon.get_name()}")
            break


# demo de combate
# print(f"{primer_pokemo.name_pokemon}:", primer_pokemo.get_hp(), "vs", f"{segundo_pokemom.name_pokemon}:",
#       segundo_pokemom.get_hp())
#
# turno = 0
# while primer_pokemo.get_hp() > 0 and segundo_pokemom.get_hp() > 0:
#     if turno == 0:
#         # turno del primer
#         ataque = segundo_pokemom.damages
#         primer_pokemo.set_damages_received(ataque)
#         print(f"{primer_pokemo.name_pokemon}:", primer_pokemo.get_hp())
#         turno += 1
#     if turno == 1:
#         # turno de pokemon
#         ataque = primer_pokemo.damages
#         segundo_pokemom.set_damages_received(ataque)
#         print(f"{segundo_pokemom.name_pokemon}:", segundo_pokemom.get_hp())
#         turno -= 1
#
# if primer_pokemo.health_point <= 0:
#     print(f"{primer_pokemo.name_pokemon} ha sido debilitado")
# else:
#     print(f"{segundo_pokemom.name_pokemon} ha sido debilitado")
