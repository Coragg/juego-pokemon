class DatosBasico:
    name_pokemon: str
    tipos: list
    hp: int
    damages: int
    level: int
    velocidad: int

    def __init__(self, name, hp, damages):
        self.name_pokemon = name
        self.hp = hp
        self.damages = damages


    def set_hp(self, vida):
        self.hp = vida

    def get_hp(self, vida):
        return vida





lista = []