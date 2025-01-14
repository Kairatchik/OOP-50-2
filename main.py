# # OOP
#
# # First Class
#
# # add_number
# # AddNumber -
#
# # Класс
# class Person:
#     # Магикеский метод
#     def __init__(self, name, age=0, city="None"):
#         # Атрибуты класса
#         self.name = name
#         self.age = age
#         self.city = city
#
#
#     def introduce(self):
#         print(f"Привет меня зовут {self.name}, мне {self.age}, я живу в городе {self.city}")
#
#     def __str__(self):
#         return f"Вернул имя объекта {self.name}"
#
# # Объекты класса / Экземплярами класса
# person_first = Person("Ардагер", 25, "с.Сокулук")
# person_second = Person(name="John Doe", age=33, city="None")
#
# print(person_first.age)
# person_first.introduce()
# print(person_second)


import random
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.__random_int = random.randint(1, 3)

    def attack(self):
        return f"{self.name} атакует с силой {self.strength}."

    def protection(self):
        return f"{self.name} защищается, сохраняя здоровье {self.health}."

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Теперь здоровье: {self.health}."

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
