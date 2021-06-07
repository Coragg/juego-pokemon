class DatosBasico:
    name_pokemon: str
    tipo_de_pokemon: str
    hp: int
    damages: int
    level: int
    velocidad: int
    velodidad_de_ataque = int

    def __init__(self, name, helth_point, damages):
        self.name_pokemon = name
        self.hp = helth_point
        self.damages = damages

    def get_hp(self):
        return self.hp

    def get_damages(self):
        return self.damages

    def set_dagno_recibido(self, dagno):
        self.hp -= dagno

    def get_dagno_recibido(self):
        return self.hp

    def set_tipo_pokemon(self, tipo):
        self.tipo_de_pokemon = tipo

    def get_tipo_pokemon(self):
        return self.tipo_de_pokemon

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad_de_ataque(self, velocidad):
        self.set_velocidad_de_ataque = velocidad



