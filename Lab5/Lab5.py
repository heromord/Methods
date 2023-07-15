from abc import ABC, abstractmethod


class IProduct(ABC):
    """
    Интерфейс продуктов
    из меню с абстрактными
    методами цена и имя
    """
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Product(IProduct):
    """
    Класс продукта
    в нем определены
    методы цена и имя
    а так же определен
    конструктор
    """
    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoundProduct(IProduct):
    """
    Класс компонуемых продуктов
    в нем определены
    методы цена и имя
    реализованы методы
    удаления продукта
    добавление продукта
    и очищение "корзины"
    а так же определен
    конструктор
    """
    def __init__(self, name: str):
        self.__name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        print(f"Стоимость '{self.name()}' = {cost} $")
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product(self, product: IProduct):
        self.products.remove(product)

    def clear(self):
        self.products = []


class Menu(CompoundProduct):
    """
    Класс Заказа относледованный
    от класса компануемых продуктов
    переопределяет метод кост для
    "красивого" вывода компануемого
    объекта с уровнем вложенности
    не более 2
    """
    def __init__(self, name: str):
        super(Menu, self).__init__(name)

    def cost(self):
        cost = 0
        cost_i = 0
        for it in self.products:
            print(it.name())
            for i in it.products:
                cost_i = i.cost()
                print(f"Стоимость '{i.name()}' = {cost_i} $")
                cost += cost_i
        print(f"Cost '{self.name()}' = {cost} $")
        return cost


if __name__ == "__main__":
    Menu = Menu("Меню")
    Bar = CompoundProduct("Бар")
    Kitchen = CompoundProduct("Кухня")
    Bar.add_product(Product("Мартини", 12))
    Bar.add_product(Product("ВодкаПиво", 10))
    Kitchen.add_product(Product("МясоПоМиэмовски", 5))
    Kitchen.add_product(Product("НормальноеМясо", 6))
    Menu.add_product(Bar)
    Menu.add_product(Kitchen)
    Menu.cost()
