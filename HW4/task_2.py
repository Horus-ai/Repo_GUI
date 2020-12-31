"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit
from random import randint

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

num_1 = randint(1000, 100000)
num_2 = randint(10000000, 1000000000000)

print('Без сохранения данных')
print(
    timeit(
        "recursive_reverse(num_1)",
        setup='from __main__ import recursive_reverse, num_1',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_2)",
        setup='from __main__ import recursive_reverse, num_2',
        number=10000))

""""
Без сохранения данных
0.016786099999999998
0.04514529999999999


Чтобы коду не приходилось каждый раз пересчитывать значения можно использовать свойсвто фунцкии Мемризация, 
для сохранениия (кэширования) подсчетов

def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Использование кэширования')
print(
    timeit(
        'recursive_reverse_mem(num_1)',
        setup='from __main__ import recursive_reverse_mem, num_1',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_2)',
        setup='from __main__ import recursive_reverse_mem, num_2',
        number=10000))

"""
Использование кэширования
0.001775799999999994
0.002800799999999992

Используя кэширование получилось скоратить разницу во времени между малыми и большими значениями, 
хоть и не удалось уровнять их

