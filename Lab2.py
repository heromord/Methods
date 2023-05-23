from Lab1 import FlightsArr
from Lab1 import quick_sort
import datetime
import time
import multidict

def Linear_serch(arr: list, object) -> int:
    """
           Линейный поиск
           :param arr: массив объктов класса  FlightsArr в котором происходит поиск
           :type arr: list
           :param object: ключ по которому ищем объект
           :type object: string
           :return: номер первого вхождения искомого обекта
           :rtype: int
    """
    for i in range(len(arr)):      # проходим массив с первого элемента по последний
       if(arr[i].name == object):  # сравниваем эллемент массива с ключом
            return i               # возвращаем номер найденного элемента
    return -1                      # возвращаем -1 если элемент не найден

def Binary_serch_withoutsort(arr: list, object)-> int:
    """
               Бинарный поиск у уже отсортированном массиве
               :param arr: массив объктов класса  FlightsArr в котором происходит поиск
               :type arr: list
               :param object: ключ по которому ищем объект
               :type object: string
               :return: номер первого вхождения искомого обекта
               :rtype: int
    """
    first = 0                                   # Индекс первого элемента
    last = len(arr)-1                           # Индекс последнего элемента
    index = -1                                  # Номер искомого элемента
    while (first <= last) and (index == -1):    # Пока индекс поледнего элемента не равен индексу первого элемента или индекс искомого элемента равен не -1
        mid = (first+last)//2                   # Индекс среднего элемента
        if arr[mid].name == object:             # Если ключ равено среднему элементу
            index = mid                         # Номер искомого элемента равен индексу среднегого
        else:                                   # Иначе
            if object < arr[mid].name:          # Если номер искомого элемента больше индекса среднегого
                last = mid - 1                  # Индекс последнего элмента становится равен индексу среднего элемента -1
            else:                               # Иначе
                first = mid + 1                 # Индекс первого элмента становится равен индексу среднего элемента + 1
    return index                                # Возвращаем индекс найденного элемента или -1 если такого нет

def Binary_serch_withsort(arr: list, object)->int:
    """
               Бинарный поиск с быстрой сортировкой
               :param arr: массив объктов класса  FlightsArr в котором происходит поиск
               :type arr: list
               :param object: ключ по которому ищем объект
               :type object: string
               :return: номер первого вхождения искомого обекта
               :rtype: int
    """
    arr_copy = quick_sort(arr)                 # Сортируем исходный массив быстрой сортировкой
    first = 0                                  # Индекс первого элемента
    last = len(arr_copy) - 1                   # Индекс последнего элемента
    index = -1                                 # Номер искомого элемента
    while (first <= last) and (index == -1):   # Пока индекс поледнего элемента не равен индексу первого элемента или индекс искомого элемента равен не -1
        mid = (first + last) // 2              # Индекс среднего элемента
        if arr_copy[mid].name == object:       # Если ключ равено среднему элементу
            index = mid                        # Номер искомого элемента равен индексу среднегого
        else:                                  # Иначе
            if object < arr_copy[mid].name:    # Если номер искомого элемента больше индекса среднегого
                last = mid - 1                 # Индекс последнего элмента становится равен индексу среднего элемента -1
            else:                              # Иначе
                first = mid + 1                # Индекс первого элмента становится равен индексу среднего элемента + 1
    return index                               # Возвращаем индекс найденного элемента или -1 если такого нет





if __name__ == '__main__':
    for n in [100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 100000]:
        arr = []
        with open(f"db_{n}.txt", "r") as db:
            data = db.read()
        data_lst = data.split("\n")
        for i in data_lst[:-1]:
            per = i.split("--")
            per[-3] = datetime.date.fromisoformat(per[-3])
            per[-2] = datetime.time.fromisoformat(per[-2])
            per[-1] = int(per[-1])
            arr.append(FlightsArr(*per))
        print(f"{n}:")

        t_start_1 = time.perf_counter()
        linear = Linear_serch(arr.copy(), "Fake")
        all_time_1 = time.perf_counter() - t_start_1
        print(f"Линейный поиск {all_time_1}")

        arr_copy = quick_sort(arr.copy())
        t_start_2 = time.perf_counter()
        binary = Binary_serch_withoutsort(arr_copy, "Fake")
        all_time_2 = time.perf_counter() - t_start_2
        print(f"Бинарный поиск в сортированно массиве {all_time_2}")

        t_start_3 = time.perf_counter()
        binaryws = Binary_serch_withsort(arr.copy(), "Fake")
        all_time_3 = time.perf_counter() - t_start_3
        print(f"Бинарный писк с бытрой сортировкой  {all_time_3}")

        d = multidict.MultiDict()
        for i in range(len(arr)):
            d.add(str(arr[i].name), i)
        t_start_4 = time.perf_counter()
        mul_dic = d.get("fake", -1)
        all_time_4 = time.perf_counter() - t_start_4
        print(f"Поиск по словарю  {all_time_4}")