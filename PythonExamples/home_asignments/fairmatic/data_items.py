class Product:
    def __init__(self, product_id, product_name, aisle_id, department_id):
        self.product_id = product_id
        self.product_name = product_name
        self.aisle_id = aisle_id
        self.department_id = department_id

class Department:
    def __init__(self, department_id, department):
        self.department_id = department_id
        self.department = department

class Order:
    def __init__(self, order_id, user_id, eval_set, order_number, order_dow, order_hour_of_day, days_since_prior_order):
        self.order_id = order_id
        self.user_id = user_id
        self.eval_set = eval_set
        self.order_number = order_number
        self.order_dow = order_dow
        self.order_hour_of_day = order_hour_of_day
        self.days_since_prior_order = days_since_prior_order
