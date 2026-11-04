import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def attack(self, other):
        atk_power = int((random.randint(30, 90) / 100) * self.attack_power)
        if other.is_alive():
            other.hp -= atk_power
            print(f"{self.name} attacks {other.name} for {atk_power} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"

