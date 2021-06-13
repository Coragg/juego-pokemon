import random
import math


def health_point(base):
    level, iv, ev = 50, 31, 250
    hp = (((((base + iv) * 2) + ((math.sqrt(ev)) / 4)) * level) / 100) + level + 10
    return hp


def other_stat(base):
    level, iv, ev = 50, 31, 250
    calculate_other_stat = (((((base + iv) * 2) + ((math.sqrt(ev)) / 4)) * level) / 100) + 5
    return calculate_other_stat


def modifier(type_pokemon, stab):
    random_decimal = random.uniform(0.85, 1)
    calculate_modifier = type_pokemon * stab * random_decimal * 1
    return round(calculate_modifier, 2)


def damages(power, type_pokemon, stab, ataque, defensa_enemigo):
    level = 50
    use_modifier = modifier(type_pokemon, stab)
    calculo = (((((2 * level) / 5) + 2) * power * (ataque / defensa_enemigo) / 50) + 2) * use_modifier
    return calculo

