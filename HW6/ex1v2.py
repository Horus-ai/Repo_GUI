import timeit
from functools import reduce
from memory_profiler import profile, memory_usage


def memory_checker(func):
    def start(*args, **kwargs):

        mem_diff = []
        for i in range(5):

            m1 = memory_usage()
            print(f'm1 - {m1}')

            func(args[0])


            m2 = memory_usage()

            print(f'm2 - {m2}')

            mem_diff.append(m2[0] - m1[0])

        print(f'{sum(mem_diff)/5} Mib')
    return start


@memory_checker

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
print(eratosfen(i))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen, i", number=1000))

"""
Не совсем понимаю как работет данный подсчет(после запуска программы он продолжает выполнять подсчеты)
Результат:
m1 - [18.8125]
m2 - [19.0234375]
m1 - [19.0234375]
m2 - [19.0234375]
m1 - [19.0234375]
m2 - [19.0234375]
m1 - [19.0234375]
m2 - [19.0234375]
m1 - [19.0234375]
m2 - [19.0234375]
0.0421875 Mib
None
m1 - [19.03125]
m2 - [19.03515625]
m1 - [19.03515625]
m2 - [19.03515625]
m1 - [19.03515625]
m2 - [19.03515625]
m1 - [19.03515625]
m2 - [19.03515625]
m1 - [19.03515625]
m2 - [19.03515625]
0.00078125 Mib
m1 - [19.03515625]
m2 - [19.03515625]
m1 - [19.03515625]
m2 - [19.03515625]
m1 - [19.03515625]
m2 - [19.0390625]
m1 - [19.0390625]
m2 - [19.0390625]
m1 - [19.0390625]
m2 - [19.0390625]
0.00078125 Mib
m1 - [19.0390625]
m2 - [19.0390625]
m1 - [19.0390625]
m2 - [19.0390625]
m1 - [19.0390625]
m2 - [19.0390625]
m1 - [19.0390625]
m2 - [19.0390625]
m1 - [19.0390625]
m2 - [19.0390625]
0.0 Mib
"""