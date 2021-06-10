class CaracteristicasPokemon:
    name: str
    class_pokemon: str
    hp: eval
    attack: eval
    level = 50
    velocity: eval
    defense: eval

    def __init__(self, name, health_point, damages):
        self.name = name
        self.hp = health_point
        self.attack = damages

    def get_hp(self):
        return self.hp

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_attack(self, damages):
        self.attack = damages

    def get_attack(self):
        return self.attack

    def set_damages_received(self, damages):
        self.hp -= damages

    def set_type_pokemon(self, type_pokemon):
        self.class_pokemon = type_pokemon

    def get_type_pokemon(self):
        return self.class_pokemon

    def set_velocity(self, velocity):
        self.velocity = velocity

    def get_velocity(self):
        return self.velocity

    def set_defense(self, defending):
        self.defense = defending

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level
