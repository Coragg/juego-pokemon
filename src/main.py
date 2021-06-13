from datos_pokemo import caracteristicas_pokemon as info_poke
from src import read_document as leer

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

data_pokemon = leer.data_of_pokemons()
nombre_primer_pokemon = input("Elija su pokemon: ")
search_pokemon = leer.buscar_nombre(nombre_primer_pokemon, data_pokemon)
while search_pokemon == False:
      nombre_primer_pokemon = input("Elija su pokemon: ")
      search_pokemon = leer.buscar_nombre(nombre_primer_pokemon, data_pokemon)

primer_pokemon = info_poke.CaracteristicasPokemon()
primer_pokemon.set_name(data_pokemon[search_pokemon][0])

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
leer.mostrar_habilidades(search_pokemon, data_pokemon)
seleccionar_ataque = int(input("Seleccione un ataque a ejecutar: "))

print(f"El ataque seleccionado es:  {seleccionar_ataque}")
print(f"El hp al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {None}")
print(f"El atk al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {None}")
print(f"El def al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {None}")
print(f"El spa al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {None}")
print(f"El spd al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {None}")
print(f"El spe al nivel {primer_pokemon.get_level()} de {primer_pokemon.get_name()} es {None}")

segundo_poke = input("Nombre del Pokémon seleccionado:   ")
segundo_pokemon = info_poke.CaracteristicasPokemon()
print(f"El hp al nivel {segundo_pokemon.get_level()} de {segundo_pokemon.get_name()} es {None}")
print(f"El daño que realizó  {primer_pokemon.get_name()} a {segundo_pokemon.get_name()} fue de: {None}")

print(f"{segundo_pokemon.name} quedó con un health_point de: {None}")

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
