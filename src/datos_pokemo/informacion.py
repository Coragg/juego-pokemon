class DatosBasico:
    name_pokemon: str
    tipo_de_pokemon: list
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

    def get_hp(self):
        return self.hp

    def get_damages(self):
        return self.damages


    def set_dagno_recibido(self, dagno):
        self.hp -= dagno

    def get_dagno_recibido(self):
        return self.hp





lista = []