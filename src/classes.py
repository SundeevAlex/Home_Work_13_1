from abc import ABC, abstractmethod


class Category:
    """Класс категории"""
    count_of_category = 0
    unique_goods = 0
    list_goods = []

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.count_of_category += 1

    def add_list_good(self, goods):
        """
        добавление товаров в категорию
        """
        if isinstance(goods, Product):
            self.list_goods.append(goods)

    # def add_product(self, data, new_good):
    #     """Добавление в список продуктов нового продукта"""
    #     if isinstance(new_good, Product) or issubclass(new_good.__class__, Product):
    #         data.append(new_good)
    #         return data
    #     else:
    #         raise TypeError("Не является объектом Product или его наследником")x
    @property
    def print_goods(self):
        """
        геттер, который выводит список товаров
        """
        result = ''
        for i in range(0, len(self.list_goods)):
            for j in range(0, len(self.list_goods[i])):
                result += (f'{self.list_goods[i][j]['name']}, {int(self.list_goods[i][j]['price'])} руб. '
                           f'Остаток: {self.list_goods[i][j]['quantity']} шт.\n')
        return result

    def __len__(self):
        """
        Определение количества продуктов на складе
        """
        return len(self.__goods)

    def __str__(self):
        return f'{self.name}, количество продуктов:'

    def __repr__(self):
        return (f"Category: ('{self.name}', {self.description}, '{self.__goods}', "
                f"'общее количество категорий={self.count_of_category} "
                f"количество уникальных продуктов={self.unique_goods}')")


class BaseProduct(ABC):

    @abstractmethod
    def new_goods(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def prices(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class MixinRepr:

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'Создан объект --> {self.__class__.__name__}, {self.__dict__.items()}'


class Product(MixinRepr, BaseProduct):
    """Класс продукт"""
    count_of_products = 0
    new_good = []

    def __init__(self, name: str, description: str, price: float, quantity: int, color='No'):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

        Product.count_of_products += 1

    def new_goods(self, name: str, description: str, price: float, quantity: int):
        """
        создание товара
        """
        new_good = name, description, price, quantity
        return new_good

    # @staticmethod
    # def add_product(self, data, new_good):
    #     """Добавление в список продуктов нового продукта"""
    #     if isinstance(new_good, Product) or issubclass(new_good.__class__, Product):
    #         data.append(new_good)
    #         return data
    #     else:
    #         raise TypeError("Не является объектом Product или его наследником")

    @property
    def prices(self):
        return self.__price

    @prices.setter
    def prices(self, new_price):
        """
        Установка новой цены
        """
        if new_price == self.__price or new_price <= 0:
            print('Цена введена некорректная!')
        elif new_price < self.__price:
            choice = input('Введенная цена ниже установленой!\nСогласны понизить цену? (Y/N): ')
            if choice.upper() == 'Y':
                self.__price = new_price
        else:
            self.__price = new_price

    @prices.deleter
    def prices(self):
        self.__price = None
        # or del self.__price

    def __add__(self, other):
        """
        Сложение объектов между собой
        """
        if isinstance(other, type(self)):
            return self.prices * self.quantity + other.prices * other.quantity
        else:
            raise TypeError

    def __str__(self):
        return f'{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт.'

    # def __repr__(self):
    #     return (f"Product: ('{self.name}', '{self.description}', '{self.__price}', "
    #             f"'Количество продуктов в наличии={self.quantity}')")


class SmartPhone(Product, MixinRepr):
    """Класс смартфон"""

    def __init__(self, efficiency: float, model: str, memory: float, name: str, description: str, price: float,
                 quantity: int, color):
        super(SmartPhone, self).__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product, MixinRepr):
    """Класс трава газонная"""

    def __init__(self, made: str, period: float, name: str, description: str, price: float, quantity: int, color):
        super(LawnGrass, self).__init__(name, description, price, quantity, color)
        self.made = made
        self.period = period


smr = SmartPhone(100, 'hjkhj', 512, 'name', 'descr', 1000, 5, 'witi')
lgr = LawnGrass('China', 6.5, 'nam', 'descrip', 850, 3, 'green')

# new_product = Product.new_goods("Sony", "мычит", 500.0, 10)
# print('Новый продукт:', new_product)
