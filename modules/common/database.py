import sqlite3 # модуль для взаємодії з бд


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(r'D:\\Pet_project_2024\\Authomation_project_2024' + r'\\become_qa_auto.db') #  connection - сутність яка потрібна модулюдля взаємодії з бд
        self.cursor = self.connection.cursor() # сутність, яка може виконувати наші команди в бд

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query) # виконуємо запит до бд щоб отримати вкрсію бд
        record = self.cursor.fetchall() # отримання результатів запиту
        print(f'Connected successfully. SQLite Database version is: {record}')

    def get_all_users(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT  address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = 'SELECT orders.id, customers.name, products.name, products.description, orders.order_date  FROM orders JOIN customers ON orders.customer_id = customers.id JOIN products ON orders.product_id = products.id'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def add_a_few_users(self):
       data = [
    (4, "Yevgen",  "Ugorska",  "Chop", "0100", "Ukraine"),
    (5, "Victor",  "Lukasha",  "Lviv", "3700", "Ukraine"),
    (6, "Ivan",  "Petefi",  "Uzhgorod", "90300", "Ukraine"),
]
       self.cursor.executemany("INSERT OR REPLACE INTO customers VALUES (?, ?, ?, ?, ?, ?)", data) #замість '' використовуємо ? кількість якого = кількості стовпців таблиці
       self.connection.commit()

    def add_to_add_user_with_the_invalid_unique_parametr(self):
       data = [
    (4, "Taras",  "Mala Polova",  "Vinogradiv", "90300", "Ukraine"),

]
       self.cursor.executemany("INSERT OR REPLACE INTO customers VALUES (?, ?, ?, ?, ?, ?)", data) #замість '' використовуємо ? кількість якого = кількості стовпців таблиці
       self.connection.commit()