from faker import Faker
from Lab1 import FlightsArr
import random

faker = Faker()

Company = {"Компания": ["AiroFlot", "Pobeda", "TurkichAirlains", "NordVind", "S7", "JoPanAirlains", "AmogusAir"]}

def gen(n):
    """
    Генерирует n записей вида id-Компания-Дата_прилета-Время_прилета-Кол_во_пассажиров

    :param n: количество генерируемых записей
    :type n: int
    :return lst: список сгенерированных записей
    :rtype lst: list
    """
    lst = []
    for _ in range(n):
        lst.append(str(str(random.randint(0, 1000)) + "--" + (str(faker.unique.name()).replace(" ", "")).lower() + "--" +
                       str(faker.date_this_month()) + "--" + str(faker.time()) + "--" + str(random.randint(1, 300))
                       + "--" + "None" + "--" + "None"))
    return lst


if __name__ == "__main__":
    selections_lst = [100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 100000]
    for j in selections_lst:
        with open(f"db_{j}.txt", "w") as db:
            for i in gen(j):
                db.write(i + "\n")