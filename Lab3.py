from Lab1 import FlightsArr
import datetime
import time
from collections import deque

def Hash(object) -> int:
    hash = 0
    p = 29
    p_pow = 1
    str = object
    for i in range(len(str)):
       hash = (ord(str[i])-ord('a') + 1) + p_pow
       p_pow *= p
    return hash % (2**64)

def HardHash(object) -> int:
    str = object
    hash = 0
    for i in range(len(str)):
        hash = ((hash * 1664525) + (ord(str[i])-ord('a')) + 1013904223)   # ord возвращает код элемента
    return hash % (2**64)

def HashTable (massiv):
    ct = 0
    d = {}
    count = len(massiv)
    for i in range(count):
        if d.get(Hash(massiv[i].name), 0) == 0 :
            dq = deque([massiv[i].name])
            d.update([(Hash(massiv[i].name), dq)])
        else:
            spisok = d.get(Hash(massiv[i].name), 0)
            if spisok.count(massiv[i].name) != 0:
                None
            else:
                ct += 1
                dq = deque()
                dq.extend(spisok)
                dq.append(massiv[i].name)
                d.update([(Hash(massiv[i].name), dq)])

    return [d, ct]

def serchHash(hashdict, serch):
    hash = Hash(serch)
    if hashdict.get(hash, 0) == 0:
        return 0
    else:
        dq = hashdict.get(hash, 0)
        return dq.count(serch)

def serchHashHard(hashdict, serch):
    hash = HardHash(serch)
    if hashdict.get(hash, 0) == 0:
        return 0
    else:
        dq = hashdict.get(hash, 0)
        return dq.count(serch)



def HashTableHard (massiv):
    d = {}
    ct = 0
    count = len(massiv)
    for i in range(count):
        if d.get(HardHash(massiv[i].name), 0) == 0 :
            dq = deque([massiv[i].name])
            d.update([(HardHash(massiv[i].name), dq)])
        else:
            spisok = d.get(HardHash(massiv[i].name), 0)
            if spisok.count(massiv[i].name) != 0:
                None
            else:
                ct += 1
                dq = deque()
                dq.extend(spisok)
                dq.append(massiv[i].name)
                d.update([(HardHash(massiv[i].name), dq)])

    return [d, ct]

if __name__ == '__main__':
 for n in [100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 100000]:
    arr = []
    with open(f"db_{n}.txt", "r") as db:
        data = db.read()
    data_lst = data.split("\n")
    for i in data_lst[:-1]:
        per = i.split("--")
        per[-5] = datetime.date.fromisoformat(per[-5])
        per[-4] = datetime.time.fromisoformat(per[-4])
        per[-3] = int(per[-3])
        per[-2] = Hash(str(per[-6]))
        per[-1] = HardHash(str(per[-6]))
        arr.append(FlightsArr(*per))
    print(f"{n}:")
    print(f"Колизий просто")
    DICT1 = HashTable(arr)
    print(DICT1[1])
    print(f"Колизий сложно")
    DICT2 = HashTableHard(arr)
    print(DICT2[1])
    t_start_1 = time.perf_counter()
    serchHash(DICT1[0], "cannon")
    all_time_1 = time.perf_counter() - t_start_1
    print(f"Поиск просто {all_time_1}")

    t_start_2 = time.perf_counter()
    serchHashHard(DICT2[0], "cannon")
    all_time_2 = time.perf_counter() - t_start_2
    print(f"Поиск сложно {all_time_2}")
