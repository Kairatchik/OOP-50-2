class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

hero1 = Hero(name="Артур", lvl=5, HP=100)
hero2 = Hero(name="Ланселот", lvl=12, HP=150)
hero3 = Hero(name="Гвен", lvl=10, HP=120)

hero1.introduce()
print(hero1.is_adult())

hero2.introduce()
print(hero2.is_adult())

hero3.introduce()
print(hero3.is_adult())
