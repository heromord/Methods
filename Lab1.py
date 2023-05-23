import datetime
import random


class FlightsArr:
    def __init__(self, id, name, date, time, number):
        """
        Конструктор класса Flights_Arr
        :param id:
        :param name:
        :param date:
        :param time:
        :param number:
        """
        self.id = id
        self.name = name
        self.date = date
        self.time = time
        self.number = number

    def __lt__(self, other):
        """
        Перегрузка оператора меньше
        :param other: Объект класса :class: `Flights_Arr`, с которым проводится сравнение
        :type other: :class: `Flights_Arr`
        :return: True, если данный объект меньше объекта other, иначе False
        :rtype: bool
        """
        if self.date < other.date:
            return True
        elif self.date == other.date:
            if self.time < other.time:
                return True
            elif self.time == other.time:
                if self.name < other.name:
                    return True
                elif self.name == other.name:
                    if self.number > other.number:
                        return True
        return False

    def __le__(self, other):
        """
        Перегрузка оператора меньше или равно
        :param other: Объект класса :class: `Flights_Arr`, с которым проводится сравнение
        :type other: :class: `Flights_Arr`
        :return: True, если данный объект меньше или равен объекта other, иначе False
        :rtype: bool
        """
        return self.__lt__(other) or (self.date == other.date and
                                      self.time == other.time and
                                      self.name == other.name and
                                      self.number == other.number)

    def __gt__(self, other):
        """
        Перегрузка оператора больше
        :param other: Объект класса :class: `FlightsArr`, с которым проводится сравнение
        :type other: :class: `FlightsArr`
        :return: True, если данный объект больше объекта other, иначе False
        :rtype: bool
        """
        return not self.__le__(other)

    def __ge__(self, other):
        """
        Перегрузка оператора больше или равно
        :param other: Объект класса :class: `Flights_Arr`, с которым проводится сравнение
        :type other: :class: `Flights_Arr`
        :return: True, если данный объект больше или равен объекта other, иначе False
        :rtype: bool
        """
        return not self.__lt__(other)

    def __str__(self):
        """
        Строковое представление объекта
        :return: строковое представление
        :rtype: str
        """
        return str(self.id) + " " + self.name + " " + str(self.date) + " " + str(self.time) + " " + str(self.number)

    def __repr__(self):
        return self.__str__()


def bubble_sort(arr: list) -> list:
    """
    Сортировка пузырьком
    :param arr: Массив для сортировки
    :type arr: list
    :return arr: Отсортированный массив
    :rtype: list
    """
    N = len(arr)-1                                       # индекс последнего элемента
    for i in range(N):                                   # идём от начала до конца массива
        for j in range(N):                               # проходим от начала до конца массива N раз
            if(arr[j] > arr[j+1]):                       # если j элемент массива больше j+1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # меняем значение jго элемена на j+1-ый и наоборот
    return arr                                           # возвращаем отсортированный массив




def cocktail_shaker_sort(arr: list) -> list:
    """
    Шейкер сортировка
    :param arr: Массив для сортировки
    :type arr: list
    :return: Отсортированный массив
    :rtype: list
    """
    left = 0                                             # индекс крайнего-левого элемента массива
    right = len(arr) - 1                                 # индекс крайнего-правого элемента массива
    while left <= right:                                 # пока индекс первого элемента меньше последнего
        for i in range(left, right, +1):                 # идем от left до right с шагом один
            if arr[i] > arr[i + 1]:                      # если i элемент больше i+1-го
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # меняем местами i и i+1-ый элементы
        right -= 1                                       # сдвигаем индекс крайнего-првого элемента влево

        for i in range(right, left, -1):                 # идем от right до left с шагом один
            if arr[i - 1] > arr[i]:                      # если i-1 ый элемент больше i
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # меняем местами i и i-1 ый элементы
        left += 1                                        # сдвигаем индекс крайнего-левого элемента вправо

    return arr                                           # возвращаем отсортированный массив



def quick_sort(arr: list) -> list:
    """
    Быстрая сортировка
    :param arr: Массив для сортировки
    :type arr: list
    :return: Отсортированный массив
    :rtype: list
    """
    if len(arr) <= 1:                                     # если длина массива меньше и равна 1
        return arr                                        # возвращаем массив
    else:                                                 # иначе
        q = random.choice(arr)                            # выбираем случайное значение в массиве
    l_arr = [n for n in arr if n < q]                     # составляем массив из элементов меньше фиксированного

    e_arr = [q] * arr.count(q)                            # составляем массив из всех элементов принимащих фиксированное значение
    r_arr = [n for n in arr if n > q]                     # составляем массив из элементов больше фиксированного
    return quick_sort(l_arr) + e_arr + quick_sort(r_arr)  # рекрсивно выполнеяем программу для левого и правого массива



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

        start_time = datetime.datetime.now()
        arr_bubble = bubble_sort(arr.copy())
        end_time = datetime.datetime.now()
        print(f"Сортировка пузырьком {end_time - start_time}")
        with open(f"sorted_bubble{n}.txt", "w") as f:
            f.write(str(arr_bubble))

        start_time = datetime.datetime.now()
        arr_shake = cocktail_shaker_sort(arr.copy())
        end_time = datetime.datetime.now()
        print(f"Шейкер сортировка {end_time - start_time}")
        with open(f"sorted_shake{n}.txt", "w") as f:
            f.write(str(arr_shake))

        start_time = datetime.datetime.now()
        arr_quick = quick_sort(arr.copy())
        end_time = datetime.datetime.now()
        print(f"Быстрая сортировка {end_time - start_time}")
        with open(f"sorted_quick{n}.txt", "w") as f:
            f.write(str(arr_quick))