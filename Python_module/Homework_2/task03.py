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
    distance_history = []

    def __init__(self):
        self.direction = Speed
        self.distance = 0

    def move(self, sec=1):
        self.sec = sec
        for i in range(sec):
            speed_obj = Speed()
            self.speed = speed_obj.speed_value
            self.direction = speed_obj.direction
            self.distance += self.speed
            self.append_history_lists()
            del speed_obj

    def append_history_lists(self):
        self.route_history.append(self.direction)
        self.distance_history.append(self.distance)

    def get_distance(self):
        return f'Total distance: {self.distance}'

    def get_direction(self, sec):
        try:
            return f'Direction = {self.route_history[sec - 1]}, distance = {self.distance_history[sec - 1]}'
        except IndexError:
            return f'Total time (sec): {self.sec}. Incorrect input'


def main():
    skier = Skier()
    skier.move()  # with default value = 1
    print(skier.get_distance())
    skier.move(10)  # with user value
    print(skier.get_distance())
    print(skier.get_direction(sec=5))
    print(skier.get_direction(sec=100))


main()
