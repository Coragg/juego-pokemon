class CaracteristicasPokemon:
    def __init__(self):
        self.name = None
        self.class_pokemon = str()
        self.hp = None
        self.attack = eval
        self.special_attack = int
        self.level = 50
        self.speed = eval
        self.defense = eval
        self.special_defense = eval

    def set_hp(self, health_point):
        self.hp = health_point

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

    def set_speed(self, velocity):
        self.speed = velocity

    def get_speed(self):
        return self.speed

    def set_defense(self, defending):
        self.defense = defending

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

    def set_special_attack(self, special_attack: int):
        self.special_attack = special_attack

    def get_special_attack(self):
        return self.special_attack

    def set_special_defense(self, special_defense):
        self.special_defense = special_defense

    def get_special_defense(self):
        return self.special_defense

    def send_data(self, list_of_data: list, ruta):
        self.set_name(list_of_data[ruta][0])
        self.set_type_pokemon(list_of_data[ruta][1])
        self.set_hp(list_of_data[ruta][2])
        self.set_attack(list_of_data[ruta][3])
        self.set_defense(list_of_data[ruta][4])
        self.set_special_attack(list_of_data[ruta][5])
        self.set_special_defense(list_of_data[ruta][6])
        self.set_speed(list_of_data[ruta][7])
