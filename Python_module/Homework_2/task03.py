# Лыжник может перемещаться только в 3-х направлениях: Юг, Запад, Восток
# если он идет галсами в направлении Запад или Восток, то его скорость составляет 1 м/с
# если катится прямо вниз (Юг), то скорость выше, и равна 5 м/с
# Создайте программную модель движения лыжника и определите: 1) какое расстояние он проедет через 17 секунд спуска
# если каждую секунду он меняет направление движения случайным образом
# 2) в каком направлении он двигался каждую секунду
# Первый класс наполните характеристиками и методами лыжника.
# Второй класс используйте для параметров движения.
# Управление программой и вывод результатов производите в основной функции main
import random


class Speed:
    direction_speed = {'south': 5, 'east': 1, 'west': 1}

    def __init__(self, direction=''):
        self.direction = random.choice(list(self.direction_speed.keys()))

    @property
    def speed_value(self):
        return self.direction_speed.get(self.direction)


class Skier:
    route_history = []

    def __init__(self):
        self.distance = 0

    def move(self, sec=1):
        for i in range(sec):
            self.speed = Speed().speed_value
            self.direction = Speed().direction
            self.distance += self.speed
            self.route_history.append(self.direction)

    def get_distance(self):
        return f'Total distance: {self.distance}'

    def get_direction(self, sec):
        if sec > len(self.route_history):
            raise SecValueError(sec)
        return f'Direction = {self.route_history[sec - 1]}'


class SecValueError(Exception):
    def __init__(self, sec):
        self.sec = sec

    def __str__(self):
        return f'{self.sec} sec is invalid input'


def main():
    skier = Skier()
    skier.move()  # with default value = 1
    print(skier.get_distance())
    skier.move(10)  # with user value
    print(skier.get_distance())
    print(skier.get_direction(sec=5))
    # print(skier.get_direction(sec=100))


main()
