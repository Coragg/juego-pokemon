from datos_pokemo import caracteristicas_pokemon as info_poke
# from datos_pokemo import estadisticas


# Anibal

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::Bienvenido al simulador de combate pokemon profesional, aqui podra probar los daños que llegaria a hacer un pokemon profesional a otro           ::")
print("::Lo que debe hacer joven entrenador es: Elegir un pokemon de primera a septima generacion, el simulador te mostrara sus estadisisticas            ::")
print("::Despues tendras que elegir una habilidad que puede usar ese pokemon, despues te mostrara las estadisticas de un pokemon de categoria profesional ::")
print("::Acto seguido eligiras un pokemon para que reciba el ataque, el cual va a mostrar su estadistica de vida en modo profesional, tu pokemon          ::")
print("::Atacara al otro mostrando el daño que harian teoricamente 2 pokemones profesionales en una lucha real                                            ::")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::Reglas profecionales: Pokeones a nivel 50, IV=31 en cada estadistica, Ev=250 Total en estadisticas, dependiendo la temporada                     ::")
print("::Se permiten el uso de pokemones legendarios, pero si miticos y singularares.                                               Disfrute el simulador ::")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
primer_poke = input("Elija su pokemon:   ")
ataque = input("Elija su ataque:    ")
segundo_poke = input("Elija el pokemon a atacar:   ")
primer_pokemo = info_poke.CaracteristicasPokemon(primer_poke, 125, 45)
segundo_pokemom = info_poke.CaracteristicasPokemon(segundo_poke, 200, 35)


# victor
print("Estadisticas bases del pokémon: ")
print("\tHP =", primer_pokemo.hp)
print("\tAtaque =", primer_pokemo.get_damages())
print("\tDefensa = ")
print("\tAtaque especial =")
print("\tDefensa especial =")
print("\tVelociodad =")


print("\nMovimientos que puede aprender el pokémon: ")
print("")
seleccionar_ataque = int(input("Seleccione un ataque a ejecutar: "))

print(f"El ataque seleccionado es:  {seleccionar_ataque}")
print(f"El hp al nivel {None} de  {primer_pokemo.name_pokemon}  es  {None}")
print(f"El atk al nivel {None} de  {primer_pokemo.name_pokemon}  es  {None}")
print(f"El def al nivel {None} de {primer_pokemo.name_pokemon} es {None}")
print(f"El spa al nivel {None} de {primer_pokemo.name_pokemon} es {None}")
print(f"El spd al nivel {None} de {primer_pokemo.name_pokemon} es {None}")
print(f"El spe al nivel {None} de {primer_pokemo.name_pokemon} es {None}")







#demo de combate
# print(f"{primer_pokemo.name_pokemon}:", primer_pokemo.get_hp(), "vs", f"{segundo_pokemom.name_pokemon}:",
#       segundo_pokemom.get_hp())
#
# turno = 0
# while primer_pokemo.get_hp() > 0 and segundo_pokemom.get_hp() > 0:
#     if turno == 0:
#         # turno del primer
#         ataque = segundo_pokemom.damages
#         primer_pokemo.set_dagno_recibido(ataque)
#         print(f"{primer_pokemo.name_pokemon}:", primer_pokemo.get_hp())
#         turno += 1
#     if turno == 1:
#         # turno de pokemon
#         ataque = primer_pokemo.damages
#         segundo_pokemom.set_dagno_recibido(ataque)
#         print(f"{segundo_pokemom.name_pokemon}:", segundo_pokemom.get_hp())
#         turno -= 1
#
# if primer_pokemo.hp <= 0:
#     print(f"{primer_pokemo.name_pokemon} ha sido debilitado")
# else:
#     print(f"{segundo_pokemom.name_pokemon} ha sido debilitado")


