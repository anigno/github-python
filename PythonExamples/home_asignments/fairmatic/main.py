import csv
import os

from data_items import Product, Department, Order

class GetMilk:
    DATA_PATH = 'data'

    def __init__(self):
        self.orders = {}
        self.products = {}
        self.departments = {}
        self.results = {}

    def read_item_data(self, filename, item_dict, item_type):
        print(f'reading {filename} {item_type}')
        file = os.path.join(GetMilk.DATA_PATH, filename)
        with open(file, "r", encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for item in reader:
                    item_dict[item[0]] = item_type(*item)
            except Exception as ex:
                print(ex)

    def read_data(self):
        self.read_item_data('products.csv', self.products, Product)
        self.read_item_data('departments.csv', self.departments, Department)
        self.read_item_data('orders.csv', self.orders, Order)

    def calculate(self, filename):
        print(f'calculate {filename}')
        self.results = {}
        file = os.path.join(GetMilk.DATA_PATH, filename)
        with open(file, "r", encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            try:
                for item in reader:
                    # calculate data
                    order_id = item[0]
                    product_id = item[1]
                    order = self.orders[order_id]
                    product = self.products[product_id]
                    department = self.departments[product.department_id]
                    dow = order.order_dow
                    hour = order.order_hour_of_day
                    if dow not in self.results:
                        self.results[dow] = {}
                    if hour not in self.results[dow]:
                        self.results[dow][hour] = {}
                    if department.department not in self.results[dow][hour]:
                        self.results[dow][hour][department.department] = {}
                    self.results[dow][hour][department.department][order.user_id] = None
            except Exception as ex:
                print(f'{type(ex)}{ex.args}')

        # count departments and calculate percentage
        with open(file + '.results.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['day', 'hour', 'department(percentage%)'])
            for dow in self.results:
                for hour in self.results[dow]:
                    total = 0
                    for department in self.results[dow][hour]:
                        self.results[dow][hour][department] = len(self.results[dow][hour][department])

                        total += self.results[dow][hour][department]
                    for department in self.results[dow][hour]:
                        self.results[dow][hour][department] = self.results[dow][hour][department] * 100 // total
                        # print(f'{dow} {hour} {department} {self.results[dow][hour][department]}%')
                        writer.writerow(
                            [f'Day {dow}', f'Hour {hour}', f'{department} ({self.results[dow][hour][department]}%)'])

if __name__ == '__main__':
    gm = GetMilk()
    gm.read_data()
    # gm.calculate('order_products__prior.csv')
    gm.calculate('order_products__train.csv')
