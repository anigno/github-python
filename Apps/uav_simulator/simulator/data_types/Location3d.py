class Location3d:
    def __init__(self, x=0.0, y=0.0, h=0.0):
        self.x = x
        self.y = y
        self.h = h

    def __str__(self):
        return f'(x={self.x:.3f},y={self.y:.3f},h={self.h:.3f})'
