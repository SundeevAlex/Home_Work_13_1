import json
import os
from src.classes import Category, Product


def load_data(file_name):
    """
    Подгрузка данных по категориям и товарам из файла JSON
    """
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, "src", file_name)
    with open(PATH, encoding='UTF-8') as file:
        data = json.loads(file.read())
    return data


def print_products(data):
    """
    Для класса Product строковое отображение
    """
    for i in range(0, len(data)):
        print(data[i])


def print_categories(data):
    """
    Для класса Category строковое отображение
    """
    for i in range(0, len(data)):
        print(f'{data[i]}')


# def print_count_result(data):
#     """
#     Подсчет суммы за все имеющиеся товары
#     """
#     result = 0
#     for i in range(0, len(data)-1, 2):
#         result += data[i] + data[i+1]
#     print(f'Сумма за общее количество товара: {int(result)} руб.')


def get_category_and_product(data):
    """
    Создание объектов крассов: Категория и Продукт
    """
    categories = []
    products = []
    i = 0
    for category in data:
        categories.append(Category(category["name"], category["description"], category["products"]))
        for el in category["products"]:
            products.append(Product(el["name"], el["description"], el["price"], el["quantity"]))
            Category.unique_goods += 1
        categories[0].add_list_good(products)
        i += 1
    # print(categories[0].print_goods)
    # print_products(products)
    # print()
    # print_categories(categories)
    # print()
    # print_count_result(products)
    # new_product = Product.new_goods("Sony", "мычит", 'Simple', 950, 25)
    # print('Новый продукт:', new_product)
    return [categories, products]
