from datos_pokemo import informacion as info_poke
from datos_pokemo import estadisticas
turno = 0


primer_pokemo = info_poke.DatosBasico("Pikachu", 125, 45)
segundo_pokemom = info_poke.DatosBasico("Chakka", 200, 35)
#demo de combate
while primer_pokemo.get_hp() > 0 and segundo_pokemom.get_hp() > 0:
    if turno == 0:
        #turno de Chkka
        ataque = segundo_pokemom.damages
        primer_pokemo.set_dagno_recibido(ataque)
        print(f"{primer_pokemo.name_pokemon}:", primer_pokemo.get_hp())
        turno += 1
    if turno == 1:
        #turno de pikachu
        ataque = primer_pokemo.damages
        segundo_pokemom.set_dagno_recibido(ataque)
        print(f"{segundo_pokemom.name_pokemon}:", segundo_pokemom.get_hp())
        turno -= 1

if primer_pokemo.hp <= 0:
    print(f"{primer_pokemo.name_pokemon} ha sido debilitado")
else:
    print(f"{segundo_pokemom.name_pokemon} ha sido debilitado")