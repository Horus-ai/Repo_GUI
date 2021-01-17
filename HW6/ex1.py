import random
from timeit import timeit
from functools import reduce
from memory_profiler import profile


array = [random.randint(0, 100000) for el in range(100000)]

@profile

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
print(func_1())

"""
На выполнение кода выделено 23.6 MiB памяти, знасение инкремента равно значению используемой памяти на начало выполнения кода
При создании цикла for выделено -2815.0 MiB памяти(Что это означает? Почему значение памяти отрицательное?)
Windows 10 64bit, Python 3.9
Результат:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    9     23.6 MiB     23.6 MiB           1   @profile
    10                                         
    11                                         def func_1():
    12     23.6 MiB      0.0 MiB           1       m = 0
    13     23.6 MiB      0.0 MiB           1       num = 0
    14     23.6 MiB  -2815.0 MiB      100001       for i in array:
    15     23.6 MiB  -2815.0 MiB      100000           count = array.count(i)
    16     23.6 MiB  -2815.0 MiB      100000           if count > m:
    17     23.6 MiB      0.0 MiB           7               m = count
    18     23.6 MiB      0.0 MiB           7               num = i
    19     23.6 MiB     -0.1 MiB           2       return f'Чаще всего встречается число {num}, ' \
    20     23.6 MiB      0.0 MiB           1              f'оно появилось в массиве {m} раз(а)'


Чаще всего встречается число 69187, оно появилось в массиве 7 раз(а)
"""
