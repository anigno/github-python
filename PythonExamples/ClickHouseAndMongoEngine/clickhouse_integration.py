import time

from clickhouse_driver import Client

from PythonExamples.ClickHouseAndMongoEngine.helpers import measure_time

class ClickHouseIntegration:

    def __init__(self):
        self.client: Client = None

    def connect_to_server(self, host='localhost', port=9000, user='default', password='hclson') -> Client:
        self.client = Client(host=host, port=port, user=user, password=password)
        return self.client

    def run_query(self, query: str):
        result = self.client.execute(query)
        return result

    def create_database(self, database_name):
        query = f'CREATE DATABASE IF NOT EXISTS {database_name}'
        return self.run_query(query)

    def delete_database(self, database_name):
        query = f'DROP DATABASE IF EXISTS {database_name}'
        return self.run_query(query)

    def get_databases(self) -> list:
        query = 'SHOW DATABASES'
        result = self.run_query(query)
        databases = [row[0] for row in result]
        return databases

    def select_database(self, database_name):
        query = f'USE {database_name}'
        return self.run_query(query)

    def create_table(self, table_query: str):
        if not 'CREATE TABLE' in table_query.upper():
            raise SyntaxError('query must start with CREATE TABLE')
        return self.run_query(table_query)

    def delete_table(self, table_name: str):
        query = f'DROP TABLE IF EXISTS {table_name}'
        return self.run_query(query)

    def get_tables(self):
        query = 'SHOW TABLES'
        return self.run_query(query)

    def describe_tabel(self, table_name):
        query = f'DESCRIBE {table_name}'
        return self.run_query(query)

    # def insert_row(self, table_name, cells: tuple, values: tuple):
    #     cells = str(cells).replace("'", "")
    #     query = f'INSERT INTO {table_name} {cells} VALUES{values[1:-1]}'
    #     print(query)
    #     return self.run_query(query)

    def get_rows(self, table_name):
        query = f'SELECT * FROM {table_name}'
        return self.run_query(query)

    def export_to_csv(self, table_name, csv_filename):
        query = f"SELECT * FROM {table_name} INTO '{csv_filename}'"
        return self.run_query(query)

if __name__ == '__main__':

    ch = ClickHouseIntegration()
    client = ch.connect_to_server()
    # ch.create_database('test_database')
    print(ch.get_databases())
    database_name = 'test_database'
    ch.select_database(database_name)
    print(ch.get_tables())
    table_name = 'counter_data_map_schema'
    ch.delete_table(table_name)
    table_create_query = f'''
                CREATE TABLE {table_name} ( 
                    cell_id String, 
                    start_time DateTime, 
                    end_time DateTime, 
                    counter_data Map(String, Float32), 
                    vendor String, 
                    market String 
                ) ENGINE = MergeTree() 
                ORDER BY (start_time,end_time ) 
                PRIMARY KEY (start_time,end_time) 
                PARTITION BY market; 
            '''
    ch.create_table(table_create_query)
    print(ch.describe_tabel(table_name))

    # insert_query = "INSERT INTO counter_data_map_schema (cell_id, start_time, end_time, counter_data, vendor, market) VALUES('cell1','2023-06-18 10:00:00', '2023-06-18 12:00:00', {'counter1': 10.5, 'counter2': 20.7}, 'vendor1','market1')"
    # ch.run_query(insert_query)
    # print(ch.get_rows(table_name))

    @measure_time
    def insert_rows():
        count = 2000
        for a in range(count):
            year = 2000 + a // 100
            insert_query = f"INSERT INTO counter_data_map_schema (cell_id, start_time, end_time, counter_data, vendor, market) VALUES('cell1','{year}-06-18 10:00:00', '2023-06-18 12:00:00', {{'counter1': 10.5, 'counter2': 20.7}}, 'vendor1','market1')"
            # print(insert_query)
            ch.run_query(insert_query)

    @measure_time
    def read_rows():
        results = ch.get_rows(table_name)
        print(f'number of rows: {len(results)}')

    @measure_time
    def query_rows():
        query = f"SELECT * FROM {table_name} WHERE start_time>'2010-06-18'"
        results = ch.run_query(query)
        print(f'query number of rows: {len(results)}')

    insert_rows()
    read_rows()
    query_rows()
