class SpecialDict:
    data_dict = {}
    reset_dict = {}
    reset_value = None

    def set(self, key, value):
        self.reset_dict[key] = None
        self.data_dict[key] = value

    def get(self, key):
        if key in self.reset_dict:
            return self.data_dict[key]
        return self.reset_value

    def reset(self, value):
        # reset all values to value o(1)
        self.reset_value = value
        self.reset_dict = {}

    def init(self, value):
        for k in self.data_dict:
            self.data_dict[k] = value

if __name__ == '__main__':
    sd = SpecialDict()
    sd.set(1, 100)
    sd.set(2, 200)
    sd.set(3, 300)

    print(sd.get(2))  # 200

    sd.reset(500)
    print(sd.get(2))  # 500
    sd.set(2, 200)
    print(sd.get(2))  # 200
