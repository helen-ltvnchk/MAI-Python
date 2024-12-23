import logging
from typing import List


logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s - %(message)s")

logger = logging.getLogger(__name__)


class Product:
    def __init__(self, name: str, amount: int, price: float):
        self.name = name
        self.amount = amount
        self.price = price

    def increase_amount(self, amount: int, increase: int):
        if amount > 0:
            self.amount += increase
            logger.info(f"Количество товара {self.name} увеличено на {increase} единиц. Текущее количество: {self.amount}.")

    def decrease_amount(self, amount: int, decrease: int):
        if 0 < decrease <= self.amount:
            self.amount -= decrease
            logger.info(f"Количество товара {self.name} уменьшено на {decrease} единиц. Текущее количество: {self.amount}")
        else:
            logger.warning(f"Невозможно уменьшить количество товара {self.name} на {decrease} единиц.")

    def count_cost(self):
        return self.amount * self.price


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        logger.info(f"Товар {product.name} добавлен на склад")

    def delete_product(self, product: Product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                self.products.remove(product)
                logger.info(f"Товар {product.name} удалён со склада.")
        logger.warning(f"Товар {product.name} не найден на складе.")

    def count_total_cost(self):
        return sum(product.count_cost() for product in self.products)


class Seller:
    def __init__(self, seller_name: str):
        self.seller_name = seller_name
        self.sales_report = []
        logger.info(f"У нас новый продавец! Привет, {seller_name}")

    def sell_product(self, warehouse: Warehouse, product_name, amount):
        for product in warehouse.products:
            if product.name == product_name:
                if product_name.amount >= amount:
                    product.decrease_amount(amount)
                    sale_amount = amount * product.price
                    self.sales_report.append({
                        'product': product.name,
                        'amount': amount,
                        'total_cost': sale_amount
                    })
                    logger.info(f"{self.seller_name} продал {amount} единиц товара {product.name}")
                    return
                else:
                    logger.warning(f"Товара {product.name} недостаточно для продажи")
                    return
        logger.warning(f"Товар {product_name} отсутствует на складе")

    def generate_sales_report(self):
        logger.info(f"Отчёт о продажах продавца {self.seller_name}")
        for item in self.sales_report:
            print(f"- {sale['product']}: {sale['quantity']} шт., сумма {sale['total_cost']:.2f} руб.")
            logger.info(f"Сформирован отчёт о продажах")


# Примеры использования
if __name__ == "__main__":
    # Создаём товары
    product1 = Product('Mascara', 40, 699)
    product2 = Product('Lipstick', 54, 349)

    # Создаём склад и добавляем в него товары
    warehouse = Warehouse()
    warehouse.add_product(product1)
    warehouse.add_product(product2)

    # Создаём продавца:
    seller1 = Seller('Masha')

    # Продажа товаров
    seller1.sell_product(warehouse, 'Mascara', 3)
    seller1.sell_product(warehouse, 'Lipstick', 5)

    # Выводим отчёт о продажах
    seller1.generate_sales_report()

    # Рассчитываем общую стоимость товаров на складе
    total_cost = warehouse.count_total_cost()
    print(f"Общая стоимость товаров на складе: {total_cost:.2f} руб.")



