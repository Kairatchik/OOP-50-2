# Для выполнения задачи, выбран модуль random.
# random - это стандартный модуль Python для генерации случайных чисел и выполнения операций, связанных со случайностью.
# Он используется для создания случайных чисел, выбора случайных элементов из последовательностей, перемешивания списков и других задач.
# Преимущества random:
# - Простота в использовании.
# - Не требует установки, так как входит в стандартную библиотеку Python.
# - Подходит для базовых задач, связанных со случайностью.

import random

# Пример использования модуля random:

def generate_random_numbers(count, start, end):
    """
    Функция для генерации списка случайных чисел.

    :param count: int: Количество случайных чисел
    :param start: int: Нижняя граница диапазона
    :param end: int: Верхняя граница диапазона
    :return: list: Список случайных чисел
    """
    return [random.randint(start, end) for _ in range(count)]

def shuffle_list(input_list):
    """
    Функция для перемешивания элементов списка.

    :param input_list: list: Исходный список
    :return: list: Перемешанный список
    """
    random.shuffle(input_list)
    return input_list

# Генерация 5 случайных чисел в диапазоне от 1 до 100
random_numbers = generate_random_numbers(5, 1, 100)
print("Случайные числа:", random_numbers)

# Перемешивание списка
sample_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(sample_list)
print("Перемешанный список:", shuffled_list)
