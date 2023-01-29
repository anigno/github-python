from datetime import datetime

class TimeUtils:

    @staticmethod
    def utc_now() -> datetime:
        return datetime.utcnow()

    @staticmethod
    def local_now() -> datetime:
        return datetime.now()

    @staticmethod
    def utc_timestamp(to_int=True) -> float:
        ret = TimeUtils.utc_now().timestamp()
        return ret if not to_int else int(ret)

    @staticmethod
    def local_timestamp(to_int=True) -> float:
        ret = TimeUtils.local_now().timestamp()
        return ret if not to_int else int(ret)

    @staticmethod
    def format_time(date_time: datetime) -> str:
        return datetime.strftime(date_time, '%H:%M:%S.%f')

    @staticmethod
    def format_timestamp(timestamp: float) -> str:
        date_time = datetime.fromtimestamp(timestamp)
        return TimeUtils.format_time(date_time)

if __name__ == '__main__':
    tu = TimeUtils.utc_now()
    tl = TimeUtils.local_now()
    print(tu)
    print(tl)
    print(TimeUtils.format_time(tu))
    tu = TimeUtils.utc_timestamp(to_int=True)
    print(tu,TimeUtils.format_timestamp(tu))
