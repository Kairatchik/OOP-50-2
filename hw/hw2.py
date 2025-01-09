class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} готовится к бою."

    def attack(self):
        return f"{self.name} наносит удар!"


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            success = "успешно" if self.precision > 0.5 else "неудачно"
            return f"{self.name} выпускает стрелу! Атака {success}. Осталось стрел: {self.arrows}."
        else:
            return f"{self.name} не может атаковать! Нет стрел."

    def rest(self):
        self.arrows += 5
        return f"{self.name} пополнил запас стрел. Теперь стрел: {self.arrows}."

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}."


legolas = Archer(name="Леголас", hp=100, arrows=10, precision=0.8)

print(legolas.action())
print(legolas.attack())
print(legolas.attack())
print(legolas.rest())
print(legolas.status())
