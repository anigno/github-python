class Singleton:
    _instance = None

    @staticmethod
    def instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        self.some_data = "hello"

if __name__ == '__main__':
    a = Singleton.instance()
    b = Singleton.instance()
    print(a.some_data)
    print(b.some_data)
    a.some_data = "world"
    print(a.some_data)
    print(b.some_data)
