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


class Skier:
    route_log = []

    def __init__(self, name):
        self.name = name
        self.race_time = 17
        self.distance = 0
        self.sec = 0


class Rolling(Skier):

    def __init__(self, name):
        super().__init__(name)
        self.available_direction = ['south', 'west', 'east']
        self.get_direction()

    def get_direction(self):
        self.direction = random.choice(self.available_direction)
        self.route_log.append(self.direction)
        self.move(sec=1)

    def move(self, sec):
        self.sec += 1
        if self.sec >= self.race_time:
            self.stop()
        else:
            if self.direction == 'south':
                self.distance += 5 * sec
            else:
                self.distance += 1 * sec
            print(self.distance)  # вот здесь корректно выводится итоговая дистанция
            self.get_direction()

    def stop(self):
        return f'Race is finished. Route log: {", ".join(self.route_log)}. Distance: {self.distance}'  # а здесь уже 0 для дистанции. куда она девается? берется из __init__ класса лыжника? почему?

    def race_info(self):
        return f'Skier total distance for {self.sec} seconds: {self.distance} meters' # здесь тоже ноль + для времени гонки (ожидаю 17)


def main():
    skier = Skier('Joe')
    print(skier.name)
    Rolling(skier)
    print(Rolling.stop(skier))
    print(Rolling.race_info(skier))


main()
