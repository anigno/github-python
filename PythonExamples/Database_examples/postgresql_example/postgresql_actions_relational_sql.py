from datetime import datetime

import psycopg2
from elephantsql_db_params import db_connection_params_dict

def to_postgresql_date(date: datetime):
    return date.strftime('%Y-%m-%d')

class PostgresqlUsersTableActions:

    def __init__(self):
        self._connection = None

    def connect(self):
        try:
            self._connection = psycopg2.connect(**db_connection_params_dict)
        except psycopg2.Error as postgresql_exception:
            raise postgresql_exception
        except Exception as e:
            raise e

    def close(self):
        self._connection.close()

    def create_table_users(self):
        # Create the table query
        create_table_query = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            user_id INTEGER UNIQUE,
            name VARCHAR(255),
            available BOOLEAN,
            dateofbirth DATE
        );
        """
        cursor = self._connection.cursor()
        cursor.execute(create_table_query)
        self._connection.commit()
        cursor.close()

    def delete_table(self, tabel_name: str):
        delete_table_query = f"DROP TABLE IF EXISTS {tabel_name}"
        cursor = self._connection.cursor()
        cursor.execute(delete_table_query)
        self._connection.commit()
        cursor.close()

    def insert(self, user_id: int, name: str, available: bool, date_of_birth: datetime):
        insert_query = f"""
                    INSERT INTO users (user_id, name, available, dateofbirth)
                    VALUES ({user_id}, '{name}', {available}, '{to_postgresql_date(date_of_birth)}');
                    """
        cursor = self._connection.cursor()
        cursor.execute(insert_query)
        self._connection.commit()
        cursor.close()

    def insert2(self, user_id: int, name: str, available: bool, date_of_birth: datetime):
        insert_query = "INSERT INTO users (user_id, name, available, dateofbirth) VALUES (%s,%s,%s,%s) RETURNING id;"
        user_data = (user_id, name, available, to_postgresql_date(date_of_birth))
        cursor = self._connection.cursor()
        cursor.execute(insert_query, user_data)
        new_user_id = cursor.fetchone()[0]
        self._connection.commit()
        cursor.close()
        return new_user_id

    def read_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users;")
        all_users = cursor.fetchall()
        cursor.close()
        return all_users

    def select_user_by_user_id(self, user_id: int):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = %s;", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        return user_data

    def update_user(self, user_id: int, updated_name: str):
        cursor = self._connection.cursor()
        cursor.execute("UPDATE users SET name = %s WHERE user_id = %s;",
                       (updated_name, user_id))
        cursor.close()

    def delete_user_by_user_id(self, user_id: int):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users WHERE user_id = %s;", (user_id,))
        cursor.close()

if __name__ == '__main__':
    db = PostgresqlUsersTableActions()
    db.connect()
    db.delete_table('users')
    db.create_table_users()
    db.insert(111, 'user1', True, datetime(1975, 11, 17))
    db.insert(333, 'user3', True, datetime(1978, 5, 2))
    db.insert2(222, 'user2', False, datetime(1981, 4, 5))
    for user in db.read_all_users():
        print(user)
    print(db.select_user_by_user_id(222))
    db.update_user(111, 'new user1 name')
    print(db.select_user_by_user_id(111))
    db.delete_user_by_user_id(333)
    print()
    for user in db.read_all_users():
        print(user)
    db.close()
