from datos_pokemo import informacion as info_poke
from datos_pokemo import estadisticas



primer_pokemo = info_poke.DatosBasico("Pikachu", 125, 40)

print(primer_pokemo.hp)
primer_pokemo.set_dagno_recibido(35)
print(primer_pokemo.get_hp())
primer_pokemo.set_dagno_recibido(35)
print(primer_pokemo.get_hp())