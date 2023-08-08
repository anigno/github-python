import random
import time
from datetime import datetime, timedelta
from clickhouse_driver import Client
from PythonExamples.ClickHouseAndMongoEngine.helpers import measure_time
import csv

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

# @measure_time
def generate_and_insert_rows(table, n_cells, n_counters, start_time, end_time):
    print(f'generate_and_insert_rows {start_time} - {end_time}')
    rows = []
    for a in range(n_cells):
        market = f'market{str(a // 6000)}'
        row = [f'cell{a}',
               # datetime(random.randint(2000, 2024), 1, 2, 3, 4, 5),
               # datetime(random.randint(2000, 2024), 1, 2, 3, 4, 5),
               start_time,
               end_time,
               {'counter1': random.randint(0, 100), 'counter2': 20.7},
               f'vendor{random.randint(0, 4)}', market]
        counters: dict = row[3]
        # add counters
        for b in range(n_counters):
            counters[f'counter{b}'] = random.randint(0, 1000) / 10
        rows.append(row)
    insert_query = f'INSERT INTO {table} (cell_id, start_time, end_time, counter_data, vendor, market) VALUES '
    execute(insert_query, rows)

def generate_day_data(table, n_cells, n_counters, n_days):
    start_time = datetime(2023, 1, 1, 0, 0, 0)
    end_time = datetime(2023, 1, 1, 0, 15, 0)
    for a in range(n_days):
        for b in range(24):
            for c in range(4):
                generate_and_insert_rows(table, n_cells, n_counters, start_time, end_time)
                start_time += timedelta(minutes=15)
                end_time += timedelta(minutes=15)

def get_csv_header(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        return header_row

def generate_rows_from_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            yield row

def generate_chunks_from_rows(rows, chunk_size):
    counter = 0
    chunk_rows = []
    for row in rows:
        chunk_rows.append(row)
        counter += 1
        if counter % chunk_size == 0:
            yield chunk_rows
            chunk_rows = []
    yield chunk_rows

def create_data_row_from_chunk_row(chunk_row, header_row) -> list:
    datetime_conversion_string = '%Y-%m-%d %H:%M:%S'
    start_time = datetime.strptime(chunk_row[1], datetime_conversion_string)
    end_time = datetime.strptime(chunk_row[2], datetime_conversion_string)
    row = [chunk_row[0], start_time, end_time]
    counters_dict = {}
    for i, counter_value in enumerate(chunk_row[3:-1]):
        counters_dict[header_row[i + 3]] = float(counter_value) if counter_value != '\\N' else 0.0
    row.append(counters_dict)
    row.append(chunk_row[45])
    row.append('market_1')
    return row

def get_data_rows(chunk, header_row):
    data_rows = []
    for chunk_row in chunk:
        data_row = create_data_row_from_chunk_row(chunk_row, header_row)
        data_rows.append(data_row)
    return data_rows

def insert_chunk_rows_to_db(table, data_rows):
    print(f'inserting data rows with size: {len(data_rows)}')
    insert_query = f'INSERT INTO {table} (cell_id, start_time, end_time, counter_data, vendor, market) VALUES '
    execute(insert_query, data_rows)

def insert_from_csv(table_name):
    csv_file = '/home/aharongina/Downloads/pm_export.csv'  # 8295708 rows
    header_row = get_csv_header(csv_file)
    rows_generator = generate_rows_from_csv(csv_file)
    chunks_generator = generate_chunks_from_rows(rows_generator, 500000)
    for chunk in chunks_generator:
        data_rows = get_data_rows(chunk, header_row)
        insert_chunk_rows_to_db(table_name, data_rows)

if __name__ == '__main__':
    client = Client(host='localhost', port=9000, user='default', password='')

    execute(f'DROP DATABASE IF EXISTS sample_database')
    execute(f'CREATE DATABASE IF NOT EXISTS sample_database')
    execute(f'USE sample_database')
    execute(f'DROP TABLE IF EXISTS table_15_markets_snapshot_one')

    table_create_query = f'''
                    CREATE TABLE table_15_markets_snapshot_one (
                        cell_id String,
                        start_time DateTime,
                        end_time DateTime,
                        counter_data Map(String, Float32),
                        vendor String,
                        market String
                    ) ENGINE = MergeTree()
                    ORDER BY (start_time,cell_id )
                    PRIMARY KEY (start_time,cell_id)
                    PARTITION BY market;
                '''
    # table_create_query = f'''
    #                 CREATE TABLE {table_name} (
    #                     cell_id String,
    #                     start_time DateTime,
    #                     end_time DateTime,
    #                     counter_data Map(String, Float32),
    #                     vendor String,
    #                     market String
    #                 ) ENGINE = MergeTree()
    #                 ORDER BY (start_time,cell_id )
    #                 PRIMARY KEY (start_time,cell_id)
    #                 PARTITION BY market;
    #             '''
    execute(table_create_query)
    execute(f'SHOW TABLES')
    execute(f'DESCRIBE table_15_markets_snapshot_one')

    # generate_and_insert_rows('table_15_snapshot', 100000, 100,datetime(2023,1,1,0,0,0),datetime(2023,1,1,0,15,0))
    generate_day_data('table_15_markets_snapshot_one', 100000, 100, 1)
    # execute(f'SELECT * FROM {table_name}', is_show_list_results=False)
    # execute(f"SELECT * FROM {table_name} WHERE start_time>'2012-06-18'", is_show_list_results=False)
    # execute(f"SELECT * FROM {table_name} WHERE counter_data['counter1'] > 50", is_show_list_results=False)

    table_size_query = f'''
        SELECT table, formatReadableSize(size) as size, rows, days, formatReadableSize(avgDaySize) as avgDaySize FROM (
        SELECT
            table,
            sum(bytes) AS size,
            sum(rows) AS rows,
            min(min_date) AS min_date,
            max(max_date) AS max_date,
            (max_date - min_date) AS days,
            size / (max_date - min_date) AS avgDaySize
        FROM system.parts
        WHERE active 
        GROUP BY table
        ORDER BY rows DESC)'''
    execute(table_size_query)
