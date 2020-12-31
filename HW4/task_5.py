"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

import timeit

def simple(i):                  #O (n**2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def eratosfen(i):               # O(n log(log n))?
    """ «Решето Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


print(timeit.timeit("simple(i)", setup="from __main__ import simple, i", number=10))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen, i", number=10))


'''Введите порядковый номер искомого простого числа: 7
0.0008911000000000335
0.3659601000000001
'''


print(timeit.timeit("simple(i)", setup="from __main__ import simple, i", number=100))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen, i", number=100))

'''Введите порядковый номер искомого простого числа: 47
0.029967599999999983
0.3623742999999999'''



print(timeit.timeit("simple(i)", setup="from __main__ import simple, i", number=1000))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen, i", number=1000))


'''
Введите порядковый номер искомого простого числа: 548
3947
0.8127857999999999
0.03625429999999952

«Решето Эратосфена» оказалось более эффективным при вычислении числа с большим порядковым номером,
в остальных случаях данный алгоритьм проигрывал по скорости первому варианту.
'''