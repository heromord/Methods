from random import randint
from math import floor
import numpy as np
import time

significance_level = [0.99, 0.95, 0.90, 0.1, 0.05, 0.01]


chi_table = {
    5: [0.55, 1.15, 1.61, 9.24, 11.1, 15.1],
    8: [1.65, 2.73, 3.49, 13.4, 15.5, 20.1],
    9: [2.09, 3.33, 4.17, 14.7, 16.9, 21.7],
    12: [3.57, 5.23, 6.30, 18.5, 21.0, 26.2],
    13: [4.11, 5.89, 7.04, 19.8, 22.4, 27.7],
    15: [5.23, 7.26, 8.5, 22.3, 25.0, 30.6],
    16: [5.81, 7.98, 9.31, 23.5, 26.3, 32.0],
    19: [7.63, 10.1, 11.7, 27.2, 30.1, 36.2],
    20: [8.26, 10.9, 12.4, 28.4, 31.4, 37.6],
    21: [8.90, 11.6, 13.2, 29.6, 32.7, 38.9],
    22: [9.54, 12.63, 14.0, 30.6, 33.9, 40.3],

}

def gen(n):
    """Генерирует последовательность псевдослучайных чисел из n элементов с помощью линейного
     конгруэнтного метода в диапазоне  от 0 до 16383.

    :param n: Количество чисел, которые надо сгенерировать
    :type n: int

    :return: Возвращает массив, в котором n случайно сгенерированных чисел
    :rtype: array
    """
    # b и M взаимно простые
    # k - 1 кратно p для каждого простого p, являющегося делителем M
    # K - 1 кратно 4, если M кратно 4
    res = []
    M = 2 ** 29  # //536 870 912

    k = 71_265
    b = int(time.time() * 1_000_000)
    if b % 2 == 0:
        b += 1
    r_0 = 7

    for i in range(n):
        r_0 = (k*r_0 + b) % M
        res.append(r_0 % 16384)

    return res


def gen_fib(n):
    """Генерирует последовательность псевдослучайных чисел из n элементов с методом Фибоначчи с запозданием
     в диапазоне  от 0 до 16383.

    :param n: Количество чисел, которые надо сгенерировать
    :type n: int

    :return: Возвращает массив, в котором n случайно сгенерированных чисел
    :rtype: array
    """
    a = 97
    b = 33
    m = max(a, b)
    if n <= m:
        return gen(n)
    res = gen(m)
    for i in range(n - m):
        v = res[m + i - a] - res[m + i - b]
        if v < 0:
            v += 16383
        res.append(v)
    return res


def gen_std(n):
    """Генерирует последовательность псевдослучайных чисел из n элементов с пметода с
    помощью стандартной функции randint()
     в диапазоне  от 0 до 16383.

    :param n: Количество чисел, которые надо сгенерировать
    :type n: int

    :return: Возвращает массив, в котором n случайно сгенерированных чисел
    :rtype: array
    """
    res = []
    for i in range(n):
        res.append(randint(0, 16383))
    return res


def MeanDispersionVarianc(arr):
    """
       Считает мат ожидание, дисперсию, коэффициент вариации и делает вывод об однородности

       :param n: Количество чисел, которые надо сгенерировать
       :type n: int

       :return: Возвращает массив, в котором n случайно сгенерированных чисел
       :rtype: array
    """
    SumKv=0
    SrV=0
    SrKv=0
    varianc=0

    SrV = sum(arr)/len(arr)

    for i in range(len(arr)):
        SumKv += (arr[i]-SrV)**2

    SrKv = (SumKv/len(arr))**(0.5)
    varianc = SrKv/SrV
    if varianc > 0.1:
        return [SrV, SrKv, varianc, "НЕОДНОРОДНАЯ"]
    else:
        return [SrV, SrKv, varianc, "ОДНОРОДНАЯ"]


def chi_square(sample):
    """
    Проверяет выборку на случайность, используя критерий Хи-квадрат.

    :param sample: Выборка, для которой нужно проверить критерий хи-квадрат
    :type n: array

    :return: значение статистики, а также строковые описания
    :rtype: tuple
    """
    a, theta = 0, 16384
    n = len(sample)
    k = int(1 + np.floor(3.322*np.log10(n)))
    intervals = np.arange(a, a + theta, (theta - 1) / k)

    prob_intervals = []
    for g in range(len(intervals) - 1):
        l = np.ceil(intervals[g])
        r = np.floor(intervals[g+1])
        if intervals[g+1] == r and r != 16383:
            r -= 1
        prob_intervals.append((r-l+1) / theta)
    intervals[-1] += 1

    intervals_count = [0] * k
    for num in sample:
        for g in range(len(intervals) - 1):
            if intervals[g] <= num < intervals[g + 1]:
                intervals_count[g] += 1

    summ = 0
    for j in range(k):
        summ += intervals_count[j] ** 2 / (n * prob_intervals[j])

    v = summ - n
    z = chi_table[k - 1]
    if v < z[0]:
        return "Принимается" + f" (Уровень значимости > 0.99)", "Отвергается", v
    if v > z[-1]:
        return "Отвергается", "Отвергается", v
    r = ""
    for i in range(len(significance_level) - 1):
        if v <= z[i+1] and v >= z[i]:
            r = f" (Уровень значимости между {significance_level[i+1]} и {significance_level[i]})"
    return "Принимается" + r, "Принимается" + r, v

def aggregator(gen):
    """Данная функция генерирует выборки следующих размеров: 50, 100, 250, 500, 1000, 5_000,
    10_000, 50_000, 100_000, 1_000_000. После чего нормирует выборки и считает для каждой из
    них хаарктеристики,после чего проверяет гипотезу о случайности выборки помощью критерия
    хи-квадрат.

    :param gen: Функция, генерирующая псевдослучайную последовательность
    :type n: function
    """
    sample_sizes = [50, 500, 1000, 5_000, 10_000, 50_000,
                    100_000, 1_000_000, 2_000_000, 5_000_000]
    samples = []

    for s in sample_sizes:
        samples.append(gen(s))

    for sample in samples:
        norm_sample = list(map(lambda x: x / 16383, sample))
        MDV = MeanDispersionVarianc(norm_sample)
        mean = MDV[0]
        dispersion = MDV[1]
        variation_coefficient = MDV[2]
        print(
            f"Размер выборки: {len(sample)}\nСреднее: {round(mean, 6)}\nОтклонение: {round(dispersion, 6)}\nКоэффициент вариации: {round(variation_coefficient, 6)}\nОднородность:{MDV[3]}")
        r1, r2, val = chi_square(sample)
        print(f"Значение статистики: {round(val, 6)}")
        print(f"Гипотеза о равномерности: {r1}")
        print(f"Гипотеза о случайности: {r2}\n")

if __name__ == '__main__':

    print("Линейный конгруэнтный метод")
    aggregator(gen)
    print("Метод Фибоначчи с запаздыванием")
    aggregator(gen_fib)
    gen_times = [1000, 5000, 10000,
                 50_000, 100_000,
                 200_000, 350_000,
                 500_000, 750_000, 1_000_000]
    f1_times = []
    f2_times = []
    f3_times = []
    for g in gen_times:
        t1 = time.time()
        gen(g)
        f1_times.append(round(time.time() - t1, 6))

        t1 = time.time()
        gen_std(g)
        f2_times.append(round(time.time() - t1, 6))

        t1 = time.time()
        gen_fib(g)
        f3_times.append(round(time.time() - t1, 6))

    print("Время генерации линейного конгруэнтного метода: ", f1_times)
    print("Время генерации стандартным способом: ", f2_times)
    print("Время генерации Фибоначчи с запаздыванием: ", f3_times)