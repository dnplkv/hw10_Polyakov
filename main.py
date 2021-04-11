import collections
import itertools
from recordclass import RecordClass
from dataclasses import dataclass

import numpy as np
from numpy import genfromtxt


print("--------------------------------------------------Task 1-------------------------------------------------------")


poem = """У лукоморья дуб зелёный
Златая цепь на дубе том
И днём и ночью кот учёный
Всё ходит по цепи кругом
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит
Там на неведомых дорожках
Следы невиданных зверей
Избушка там на курьих ножках
Стоит без окон, без дверей
Там лес и дол видений полны
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской
Там королевич мимоходом
Пленяет грозного царя
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря
В темнице там царевна тужит,
А бурый волк ей верно служит
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет
Там русский дух… там Русью пахнет
И там я был, и мёд я пил
У моря видел дуб зелёный
Под ним сидел, и кот учёный
Свои мне сказки говорил."""


def most_common_letters(text):
    """Requirements implementation from item 1.

    Result: 5 most common letters
    """
    only_letters = ''.join(e for e in text if e.isalnum())
    only_lower = only_letters.lower()
    cnt = collections.Counter(only_lower)
    return print(cnt.most_common(5))


most_common_letters(poem)  # [('о', 58), ('а', 58), ('е', 51), ('т', 46), ('и', 45)]


"""Task 2
"""
Car = collections.namedtuple('Auto', ['manufacturer',
                                      'model',
                                      'height',
                                      'width',
                                      'length',
                                      'engine_power',
                                      'acceleration_time',
                                      'fuel_consumption'])

car1 = Car(manufacturer='Audi', model='A3', height=1420, width=1796, length=4458,
           engine_power=184, acceleration_time=8.4, fuel_consumption=6.1)
car2 = Car(manufacturer='BMW', model='M3', height=1370, width=1710, length=4430,
           engine_power=473, acceleration_time=4.3, fuel_consumption=8.8)
car3 = Car(manufacturer='Toyota', model='Camry', height=1455, width=1840, length=4885,
           engine_power=206, acceleration_time=7.8, fuel_consumption=8.1)
car4 = Car(manufacturer='VW', model='Passat', height=1456, width=1832, length=4767,
           engine_power=174, acceleration_time=8.7, fuel_consumption=6.5)
car5 = Car(manufacturer='Aston Martin', model='DB9', height=1270, width=1880, length=4709,
           engine_power=540, acceleration_time=4.7, fuel_consumption=14.3)
car6 = Car(manufacturer='Nissan', model='Leaf', height=1530, width=1788, length=4490,
           engine_power=147, acceleration_time=7.9, fuel_consumption=0)


print("--------------------------------------------------Task 2-------------------------------------------------------")


all_cars = [car1, car2, car3, car4, car5, car6]
for car in all_cars:
    print(car)


print("--------------------------------------------------Task 3-------------------------------------------------------")


max_height = sorted(all_cars, key=lambda car: car[2], reverse=True)
print('Top 3 cars with maximum height:')
cnt = 0
for elem in max_height:
    if cnt >= 3:
        break
    cnt += 1
    print(f'{cnt}. {elem[0]} {elem[1]} with height of {elem[2]} mm.')


max_accel = sorted(all_cars, key=lambda car: car[6])
print('Top 3 cars with best acceleration:')
cnt = 0
for elem in max_accel:
    if cnt >= 3:
        break
    cnt += 1
    print(f'{cnt}. {elem[0]} {elem[1]} with acceleration from 0-100 kph up to {elem[6]} s.')


print("--------------------------------------------------Task 4-------------------------------------------------------")


class Car(RecordClass):
    manufacturer: str
    model: str
    height: int
    width: int
    length: int
    engine_power: int
    acceleration_time: float
    fuel_consumption: float


first_car = Car('Audi', 'A3', 1420, 1796, 4458, 184, 8.4, 6.1)
second_car = Car('BMW', 'M3', 1370, 1710, 4430, 473, 4.3, 8.8)
third_car = Car('Toyota', 'Camry', 1455, 1840, 4885, 206, 7.8, 8.1)
fourth_car = Car('VW', 'Passat', 1456, 1832, 4767, 174, 8.7, 6.5)
fifth_car = Car('Aston Martin', 'DB9', 1270, 1880, 4709, 540, 4.7, 14.3)
sixth_car = Car('Nissan', 'Leaf', 1530, 1788, 4490, 147, 7.9, 0)

cars_list = [first_car, second_car, third_car, fourth_car, fifth_car, sixth_car]
best_accel = sorted(cars_list, key=lambda car: car.acceleration_time)
cnt = 0
for elem in best_accel:
    if cnt >= 3:
        break
    cnt += 1
    print(f'For {elem.manufacturer} {elem.model} with base engine power of {elem.engine_power} hp '
          f'update has been made up to {elem.engine_power + elem.engine_power * 0.1} hp.')


print("--------------------------------------------------Task 5-------------------------------------------------------")


@dataclass
class Car:
    manufacturer: str
    model: str
    height: int
    width: int
    length: int
    engine_power: int
    acceleration_time: float
    fuel_consumption: float

    def gallons_and_miles(self):
        try:
            return 235.22 / self.fuel_consumption
        except ZeroDivisionError:
            print("Your vehicle is probably an electric car")


cnt = 0
for elem in best_accel:
    if cnt >= 3:
        break
    cnt += 1
    print(f'For {elem.manufacturer} {elem.model} with fuel consumption of {elem.fuel_consumption} l/100km '
          f'were transformed to {Car.gallons_and_miles(self=elem):.2f} mpg.')


print("--------------------------------------------------Task 6-------------------------------------------------------")

cubes = list(itertools.combinations_with_replacement(range(1, 7), 2))
sum_res = list(map(sum, cubes))
cnt = collections.Counter(sum_res)
for k, v in cnt.most_common(3):
    print(f'Sum of two cubes equals to {k} and appears {v} times')

print("--------------------------------------------------Task 7-------------------------------------------------------")


my_data = genfromtxt('iris.txt', delimiter=',')
condition = np.logical_and(my_data >= 0, my_data < 3)
my_data = np.select([~condition, condition], [my_data, -my_data])
print(my_data)
