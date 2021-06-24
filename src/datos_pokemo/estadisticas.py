# Este archivo contiene las ecuaciones para el desarrollo del ataque.

import random
import math


def health_point(base):
    level, iv, ev = 50, 31, 250
    return (((((base + iv) * 2) + ((math.sqrt(ev)) / 4)) * level) / 100) + level + 10


def other_stat(base):
    level, iv, ev = 50, 31, 250
    return (((((base + iv) * 2) + ((math.sqrt(ev)) / 4)) * level) / 100) + 5


def modifier(type_pokemon: eval, stab: eval):
    random_decimal = random.uniform(0.85, 1)
    calculate_modifier = type_pokemon * stab * random_decimal * 1
    return round(calculate_modifier, 2)


def damages(power, type_pokemon, stab, attack, enemy_defense):
    level = 50
    use_modifier = modifier(type_pokemon, stab)
    return (((((2 * level) / 5) + 2) * power * (attack / enemy_defense) / 50) + 2) * use_modifier


def ataque_especial_o_ataque_fisico(power, type_pokemon, stab, attack, enemy_defense, special_attack,
                                    enemy_special_defense):
    if power[3] == 'special' or power[3] == 'status':
        return damages(power[1], type_pokemon, stab, special_attack, enemy_special_defense)
    elif power[3] == 'physical':
        return damages(power[1], type_pokemon, stab, attack, enemy_defense)
