class Direction3d:
    def __init__(self, azimuth=0.0, elevation=0.0):
        self.azimuth = azimuth
        self.elevation = elevation

    def __str__(self):
        return f'(az={self.azimuth},el={self.elevation})'
