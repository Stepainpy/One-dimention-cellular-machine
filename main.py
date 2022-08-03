"""
Это консольная версия одномерного клеточного автомата

переменные:
length_world - длина строки (если вы хотите сделать старт с одной клетки то лучше сделать его не чётным)
iterations - сколько итераций нужно пройти
rand_space - значение y или n т.е. да или нет. отвечает на вопрос сделать рандомное заполнение
rule_using - какое правило нужно использовать для работы
"""

from random import randint
import json

length_world = 101
iterations = 100
rand_space = 'n'
rule_using = 0

# проверка значения rand_space и создание относительно его начального заполнения
if rand_space == 'n':
    world = [0 for _ in range(length_world)]
    world[length_world // 2] = 1
else:
    world = [randint(0, 1) for _ in range(length_world)]

buffer = []  # нужен для создания следующей итерации

# открытия файла с правилами и запись их в переменную, а после запись только выбраного правила
with open('rules.json', 'r') as file:
    rules = json.load(file)
rule = rules[str(rule_using)]


def print_row(registry, num):
    """
    Нужна для написания нашего "мира" в консоль
    :param registry: список или точней наше поле
    :param num: число показывающее для удобства номер итерации
    """
    print('|', end='')
    for ii, s in enumerate(registry):  # перебор списка и от числа написание того или иного символа
        if ii != len(registry)-1:
            if s == 0:
                print(' ', end=' ')
            elif s == 1:
                print('■', end=' ')
        else:
            if s == 0:
                print(' ', end='')
            elif s == 1:
                print('■', end='')
    print('| '+str(num), end='')
    print()


print_row(world, 0)  # пишем начальную картину

for iteration in range(iterations):  # повторяем от значения iterations
    for i in range(length_world):  # осмотр клетки и её вместе с 2 соседями и получение значение на следующем ходе
        a, b, c = world[i-1], world[i], world[(i+1) % length_world]
        zone = str(a)+str(b)+str(c)
        buffer.append(rule[zone])

    # пишем итерацию и номер, мир делаем как получилось в буфере, а его потом делаем пустым
    print_row(buffer, iteration+1)
    world = buffer
    buffer = []
