"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):      # O(n) - линейная
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2 (nums):      # O(n) - линейная
    return [i for i, el in enumerate(nums) if el % 2 ==0]

NUMS = [el for el in range(10)]
print("1")
print(
    timeit.timeit(
        "func_1(NUMS)",
        setup = "from __main__ import func_1, NUMS",
        number = 10))

print(
    timeit.timeit(
        "func_2(NUMS)",
        setup = "from __main__ import func_2, NUMS",
        number = 10))

"""
 Результат:
 1.6800000000000842e-05
 1.4699999999999436e-05
 Итог: вариант с генерацией данных занимает меньше времени, 
 т.к выполняется меньшее количество действий
"""

NUMS2 = [el for el in range(100)]

print("2")
print(
    timeit.timeit(
        "func_1(NUMS2)",
        setup = "from __main__ import func_1, NUMS2",
        number = 100))

print(
    timeit.timeit(
        "func_2(NUMS2)",
        setup = "from __main__ import func_2, NUMS2",
        number = 100))

"""
 Результат:
 2
0.0012367000000000003
0.0011070000000000003
"""


print("3")
NUMS3 = [el for el in range(1000)]
print(
    timeit.timeit(
        "func_1(NUMS3)",
        setup = "from __main__ import func_1, NUMS3",
        number = 1000))

print(
    timeit.timeit(
        "func_2(NUMS3)",
        setup = "from __main__ import func_2, NUMS3",
        number = 1000))

"""
 Результат:
3
0.0942654
0.0771381
"""