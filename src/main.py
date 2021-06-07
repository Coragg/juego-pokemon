from datos_pokemo import informacion as info_poke
from datos_pokemo import estadisticas
turno=0


primer_pokemo = info_poke.DatosBasico("Pikachu", 125, 40)
segundo_pokemom = info_poke.DatosBasico("Chakka", 200, 35)

print(primer_pokemo.hp)
primer_pokemo.set_dagno_recibido(35)
print(primer_pokemo.get_hp())
primer_pokemo.set_dagno_recibido(35)
print(primer_pokemo.get_hp())
#demo de combate
while primer_pokemo.get_hp() > 0 and segundo_pokemom.get_hp() > 0:
    if turno == 0:
        #turno de Chkka
        ataque = segundo_pokemom.damages
        primer_pokemo.set_dagno_recibido(ataque)
        print("pikachu:", primer_pokemo.get_hp())
        if(primer_pokemo.get_hp()<=0):
            print("Pikachu ha sido debilitado")
            break
        else:
            turno += 1
    if(turno==1):
        #turno de pikachu
        segundo_pokemom.set_dagno_recibido(40)
        print("Chakka:",segundo_pokemom.get_hp())
        if(segundo_pokemom.get_hp()<=0):
            print("Chakka ha sido debilitado")
            break
        else:
            turno=turno-1