class DictWithIndex:
    dict_store = {}
    list_index_key = []
    dict_key_to_index = {}

    def __init__(self):
        pass

    def set(self, key, value):
        if key not in self.dict_store:
            self.list_index_key.append(key)
            self.dict_key_to_index[key] = len(self.list_index_key) - 1
        self.dict_store[key] = value

    def get(self, key):
        return self.dict_store[key]

    def remove(self, key):
        del (self.dict_store[key])
        i = self.dict_key_to_index[key]
        del (self.list_index_key[i])

    def get_buy_index(self, i):
        key = self.list_index_key[i]
        return self.dict_store[key]

if __name__ == '__main__':
    dw = DictWithIndex()
    dw.set(1, 100)
    dw.set(4, 400)
    dw.set(2, 200)
    dw.set(3, 300)
    print(dw.list_index_key)
    print(dw.get(2))
    print(dw.get_buy_index(2))
    dw.remove(4)
    print(dw.list_index_key)
    print(dw.get(2))
    print(dw.get_buy_index(2))

