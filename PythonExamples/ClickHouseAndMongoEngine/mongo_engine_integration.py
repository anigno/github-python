from datetime import datetime

from mongoengine import connect, Document, StringField, IntField, DictField, FloatField, DateTimeField

from PythonExamples.ClickHouseAndMongoEngine.helpers import measure_time

connect('sample_database', host='mongodb://localhost:27017')

class CounterData(Document):
    cell_id = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    counter_data = DictField(field=FloatField(), required=True)
    vendor = StringField(required=True)
    market = StringField(required=True)

if __name__ == '__main__':
    CounterData.objects().delete()

    # data = CounterData(
    #     cell_id="123",
    #     start_time=datetime(2023, 6, 1, 10, 0, 0),
    #     end_time=datetime(2023, 6, 1, 12, 0, 0),
    #     counter_data={"metric1": 10.5, "metric2": 20.3},
    #     vendor="Vendor A",
    #     market="Market X"
    # )

    @measure_time
    def insert_data():
        for a in range(2000):
            year = 2000 + a // 100
            data = CounterData(
                cell_id="123",
                start_time=datetime(year, 6, 1, 10, 0, 0),
                end_time=datetime(2023, 6, 1, 12, 0, 0),
                counter_data={"metric1": a, "metric2": 20.3},
                vendor="Vendor A",
                market="Market X"
            )
            data.save()

    @measure_time
    def read_data():
        results = CounterData.objects()
        print(f'number of rows: {len(results)}')

    @measure_time
    def query_rows():
        results = CounterData.objects(start_time__gte=datetime(2010, 6, 1, 10, 0, 0))
        print(f'query number of rows: {len(results)}')

    @measure_time
    def query_rows2():
        results = CounterData.objects(counter_data__metric1__gt=1000)
        print(f'query2 number of rows: {len(results)}')

    insert_data()
    read_data()
    query_rows()
    query_rows2()
