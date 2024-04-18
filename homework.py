import json


class Category:
    name: str
    description: str
    goods: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
        Category.total_categories += 1
        Category.total_unique_products += len(set(goods))

    def __str__(self):
        return f"Наименование категории:{self.name} Описание:{self.description} Товары:{self.goods} "

    __repr__ = __str__


class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.quantity}"

    __repr__ = __str__


def func():
    with open('examples.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)
        for category_data in data:
            category_name = category_data['name']
            category_description = category_data['description']
            category_products = []
            for product_data in category_data['products']:
                product = Product(product_data['name'], product_data['description'], product_data['price'],
                                  product_data['quantity'])
                category_products.append(product)
                print(product)
            category = Category(category_name, category_description, category_products)
            print(category)
        print(Category.total_categories)
        print(Category.total_unique_products)


def main():
    func()


main()


def test_init():
    assert Category.total_categories == 2
    assert Category.total_unique_products == 4
