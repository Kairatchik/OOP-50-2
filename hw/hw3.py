# hw3.py
from main import Hero

class Jester(Hero):
    def __init__(self, name, health, strength, humor_level):
        super().__init__(name, health, strength)
        self.humor_level = humor_level

    def unique_attack(self):
        return f"{self.name} использует уникальную атаку \"Шутка-убийца\", сила {self.humor_level + self.strength}!"

    def unique_scream(self):
        return f"{self.name} кричит: \"Смейтесь или страдайте!\""

    def action(self):
        random_int = self.get_random_int()
        if random_int == 1:
            return self.attack()
        elif random_int == 2:
            return self.protection()
        elif random_int == 3:
            return self.rest()
