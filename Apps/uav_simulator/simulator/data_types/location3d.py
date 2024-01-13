class Location3d:
    def __init__(self, x=0.0, y=0.0, h=0.0):
        self.x = x
        self.y = y
        self.h = h

    def new(self):
        """generate new Location3d instance with current fields values"""
        return Location3d(self.x, self.y, self.h)

    def __str__(self):
        return f'(x={self.x:.3f},y={self.y:.3f},h={self.h:.3f})'

if __name__ == '__main__':
    l1 = Location3d(1, 2, 3)
    l2 = l1
    l3 = l1.new()
    l1.x = 5
    l3.x = 7
    print(l1.x, l2.x, l3.x)
