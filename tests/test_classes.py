import pytest
from src.classes import Category, Product, SmartPhone, LawnGrass


@pytest.fixture
def class_category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                    [{
                        'name': "Samsung Galaxy C23 Ultra",
                        'description': "256GB, Серый цвет, 200MP камера",
                        'price': 180000.0,
                        'quantity': 5
                    }])


def test_category_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


def test_category_count_of_category(class_category):
    assert class_category.count_of_category == 2


def test_category_repr(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


@pytest.fixture
def class_products():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                   180000.0, 5)


@pytest.fixture
def class_products_add():
    return Product('Sony', 'мычит', 500.0, 7)


def test_add_product(class_products, class_products_add):
    assert isinstance(class_products_add, Product)
    assert class_products.name == 'Samsung Galaxy C23 Ultra'
    assert class_products_add.name == 'Sony'


def test___add__():
    pass


def test_products_init(class_products):
    assert class_products.name == 'Samsung Galaxy C23 Ultra'
    assert class_products.description == '256GB, Серый цвет, 200MP камера'
    assert class_products.quantity == 5


def test_products_count_of_products(class_products):
    assert class_products.count_of_products == 4


def test_products_repr(class_products):
    assert class_products.name == 'Samsung Galaxy C23 Ultra'
    assert class_products.description == '256GB, Серый цвет, 200MP камера'


def test_category_str(class_products):
    assert class_products.name == 'Samsung Galaxy C23 Ultra'
    assert class_products.prices == 180000.0


def test_print_products(class_products):
    assert class_products.name == 'Samsung Galaxy C23 Ultra'


def test_print_categories(class_category):
    assert class_category.name == 'Смартфоны'


@pytest.fixture
def class_smartphone():
    return SmartPhone(1000.5, 'TYN-5', 512.0, 'Motorolla',
                      'The best', 5000, 9, 'Silver')


def test_smartphone_init(class_smartphone):
    assert class_smartphone.efficiency == 1000.5
    assert class_smartphone.model == 'TYN-5'
    assert class_smartphone.color == 'Silver'


@pytest.fixture
def class_lawngrass():
    return LawnGrass('China', 6.5, 'Kanadka', 'For you',
                     500, 3, 'Green')


def test_lawngrass_init(class_lawngrass):
    assert class_lawngrass.made == 'China'
    assert class_lawngrass.period == 6.5
    assert class_lawngrass.color == 'Green'
