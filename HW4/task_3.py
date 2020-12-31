"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit
import cProfile

"Рекурсия"
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

"Цикл"
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

"Срез"
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

enter_num = int(input('Введите число:'))
revers(enter_num, revers_num = 0)
revers_2(enter_num, revers_num = 0)
revers_3(enter_num)

print(revers, timeit(f'revers({enter_num})',
                               setup='from __main__ import revers', number=10000))
print(revers_2, timeit(f'revers_2({enter_num})',
                               setup='from __main__ import revers_2', number=10000))
print(revers_3, timeit(f'revers_3({enter_num})',
                               setup='from __main__ import revers_3', number=10000))

# Выводятся странные значения revers, не могу понять в чем дело

cProfile.run('revers(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')



""" 
Рекурсия - 0.015246799999999894
Цикл - 0.009855499999999573
Срез - 0.002890700000000024

Из результатов видно, что в рекурсии выполняется 11 вызовов функции, в цикле и срезе - 4, 
в срезе отсутствуют арифметические выражения, что делает выполнение задачи более быстрым, чем в двух других вариантах
"""