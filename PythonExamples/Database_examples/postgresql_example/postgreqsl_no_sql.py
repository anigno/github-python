import psycopg2

from PythonExamples.Database_examples.postgresql_example.elephantsql_db_params import db_connection_params_dict

class PostgresqlKeyJson:

    def __init__(self):
        self._connection = None

    def connect(self):
        try:
            self._connection = psycopg2.connect(**db_connection_params_dict)
        except psycopg2.Error as postgresql_exception:
            raise postgresql_exception
        except Exception as e:
            raise e

    def delete_table(self):
        delete_table_query = f"DROP TABLE IF EXISTS books_json_table"
        cursor = self._connection.cursor()
        cursor.execute(delete_table_query)
        self._connection.commit()
        cursor.close()

    def create_key_json_table(self):
        create_table_query = """CREATE TABLE books_json_table (
                   id serial PRIMARY KEY,
                   book_data jsonb);"""
        cursor = self._connection.cursor()
        cursor.execute(create_table_query)
        self._connection.commit()
        cursor.close()

    def insert_data(self):
        queries = [
            """INSERT INTO books_json_table (book_data) VALUES (
            '{"title": "The Great Gatsby","author": "F. Scott Fitzgerald","year": 1925}');""",
            """INSERT INTO books_json_table (book_data) VALUES (
            '{"title": "To Kill a Mockingbird","author": "Harper Lee","year": 1960}');"""]
        for query in queries:
            cursor = self._connection.cursor()
            cursor.execute(query)
            self._connection.commit()
            cursor.close()

    def get_books_data(self):
        query = """SELECT book_data FROM books_json_table"""
        cursor = self._connection.cursor()
        cursor.execute(query)
        self._connection.commit()
        books = cursor.fetchall()
        cursor.close()
        return books

    def run_query(self, query: str):
        cursor = self._connection.cursor()
        cursor.execute(query)
        self._connection.commit()
        ret = cursor.fetchall()
        cursor.close()
        return ret

if __name__ == '__main__':
    db = PostgresqlKeyJson()
    db.connect()
    db.delete_table()
    db.create_key_json_table()
    db.insert_data()
    for book in db.get_books_data():
        print(book)
    print(db.run_query("""SELECT book_data->>'title' AS title FROM books_json_table;"""))
    print(db.run_query("""SELECT book_data->>'author' AS author FROM books_json_table;"""))
    print(db.run_query("""SELECT book_data FROM books_json_table WHERE book_data ->> 'year' = '1960';"""))
