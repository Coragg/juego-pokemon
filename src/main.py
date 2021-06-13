from datos_pokemo import caracteristicas_pokemon as info_poke
from lista_pokemon import read_document as leer
from movimiento import moves
from datos_pokemo import estadisticas

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

# Recolectar informacion del primer pokemon
search_pokemon = False
while search_pokemon == False:
      nombre_primer_pokemon = input("Elija su pokemon: ")
      search_pokemon = leer.search_name(nombre_primer_pokemon, data_pokemon, 832)

primer_pokemon = info_poke.CaracteristicasPokemon()
primer_pokemon.set_name(data_pokemon[search_pokemon][0])
primer_pokemon.set_type_pokemon(data_pokemon[search_pokemon][0])
print(f"Nombre del Pokémon seleccionado:  {primer_pokemon.get_name()}")
print("Estadisticas bases del pokémon: ")
primer_pokemon.set_hp(data_pokemon[search_pokemon][2])
print("\thp =", primer_pokemon.get_hp())
primer_pokemon.set_attack(data_pokemon[search_pokemon][3])
print("\tAtaque =", primer_pokemon.get_attack())
primer_pokemon.set_defense(data_pokemon[search_pokemon][4])
print("\tDefensa = ", primer_pokemon.get_defense())
primer_pokemon.set_special_attack(data_pokemon[search_pokemon][5])
print("\tAtaque especial =", primer_pokemon.get_special_attack())
primer_pokemon.set_special_defense(data_pokemon[search_pokemon][6])
print("\tDefensa especial =", primer_pokemon.get_special_defense())
primer_pokemon.set_velocity(data_pokemon[search_pokemon][7])
print("\tVelociodad =", primer_pokemon.get_velocity())

print("\nMovimientos que puede aprender el pokémon: ")
leer.mostrar_habilidad(search_pokemon, data_pokemon)
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
print(f"El spa al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_special_attack()}")
amplified_special_defense = estadisticas.other_stat(int(primer_pokemon.get_special_defense()))
primer_pokemon.set_special_defense(amplified_special_defense)
print(f"El spd al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_special_defense()}")
amplified_velocity = estadisticas.other_stat(int(primer_pokemon.get_velocity()))
primer_pokemon.set_velocity(amplified_velocity)
print(f"El spe al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {primer_pokemon.get_velocity()}")


# Pokemon a enfrentar
search_second_pokemon = False
while search_second_pokemon == False:
      segundo_poke = input("Ingrese el nombre del Pokémon a atacar: ")
      search_second_pokemon = leer.search_name(segundo_poke, data_pokemon, 832)

segundo_pokemon = info_poke.CaracteristicasPokemon()
segundo_pokemon.set_name(data_pokemon[search_second_pokemon][0])
print(f"Nombre del Pokémon seleccionado: {segundo_pokemon.get_name()}")
segundo_pokemon.set_hp(data_pokemon[search_second_pokemon][2])
segundo_pokemon.set_attack(data_pokemon[search_second_pokemon][3])
segundo_pokemon.set_defense(data_pokemon[search_second_pokemon][4])
segundo_pokemon.set_special_attack(data_pokemon[search_second_pokemon][5])
segundo_pokemon.set_special_defense(data_pokemon[search_second_pokemon][6])
segundo_pokemon.set_velocity(data_pokemon[search_second_pokemon][7])

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

print(f"El hp al nivel {segundo_pokemon.get_level()} de {segundo_pokemon.get_name()} es {segundo_pokemon.get_hp()}")
print(f"El daño que realizó  {primer_pokemon.get_name()} a {segundo_pokemon.get_name()} fue de: {None}")

print(f"{segundo_pokemon.name} quedó con un hp de: {None}")











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
