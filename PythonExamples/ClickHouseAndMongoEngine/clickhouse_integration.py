import random
import time
from datetime import datetime
from clickhouse_driver import Client
from PythonExamples.ClickHouseAndMongoEngine.helpers import measure_time

def execute(query, data=None, is_show_list_results=True):
    print(f'****** {query}')
    start = time.time()
    result = client.execute(query, data)
    if isinstance(result, list):
        if is_show_list_results:
            for item in result:
                print(item)
        print(f'number of items: {len(result)}')
    else:
        print(result)
    print(f'------ {time.time() - start} sec')
    print()

@measure_time
def insert_rows(table, count):
    rows = []
    for a in range(count):
        row = [f'cell{a}',
               datetime(random.randint(2000, 2024), 1, 2, 3, 4, 5),
               datetime(random.randint(2000, 2024), 1, 2, 3, 4, 5),
               {'counter1': random.randint(0, 100), 'counter2': 20.7},
               'vendor1', 'market1']
        rows.append(row)
    insert_query = f'INSERT INTO {table} (cell_id, start_time, end_time, counter_data, vendor, market) VALUES '
    execute(insert_query, rows)

if __name__ == '__main__':
    client = Client(host='localhost', port=9000, user='default', password='')
    database_name = 'sample_database'
    table_name = 'counter_data_map_schema'

    execute(f'DROP DATABASE IF EXISTS {database_name}')
    execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
    execute(f'USE {database_name}')
    execute(f'DROP TABLE IF EXISTS {table_name}')

    table_create_query = f'''
                    CREATE TABLE {table_name} (
                        start_time DateTime,
                        end_time DateTime,
                        cell_id String,
                        counter_data Map(String, Float32),
                        vendor String,
                        market String
                    ) ENGINE = MergeTree()
                    ORDER BY (start_time,end_time )
                    PRIMARY KEY (start_time,end_time)
                    PARTITION BY market;
                '''
    execute(table_create_query)

    execute(f'SHOW TABLES')
    execute(f'DESCRIBE {table_name}')

    insert_rows(table_name, 1_000_000)
    execute(f'SELECT * FROM {table_name}', is_show_list_results=False)
    execute(f"SELECT * FROM {table_name} WHERE start_time>'2012-06-18'", is_show_list_results=False)
    execute(f"SELECT * FROM {table_name} WHERE counter_data['counter1'] > 50", is_show_list_results=False)

    # def get_data_size(table_name):
    #     # query = f'''SELECT database, table, formatReadableSize(sum(data_compressed_bytes)) AS total_size
    #     #         FROM system.parts GROUP BY database, table'''
    #     # WHERE active
    #     #   AND database = 'test_database'
    #     #   AND table = '{table_name}'
    #     # GROUP BY database, table'''
    #     # query='select  * from test_database'
    #     # results = ch.run_query(query)
    #
    #     query = "SELECT formatReadableSize(database_size) AS size FROM test_database.databases WHERE name = 'test_database'"
    #     query = """
    #         SELECT sum(data_compressed_bytes) AS size
    #         FROM system.parts
    #         WHERE database = 'test_database'
    #     """
    #
    #     result = client.execute(query)
    #     print(result)
