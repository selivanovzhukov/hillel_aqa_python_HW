class Rhomb:
    def __init__(self, side_a: float, angle_a:float):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError('Side_a must be positive')
            super().__setattr__(key, value)

        elif key == 'angle_a':
            if value < 0 or value > 180:
                raise ValueError('Angle_a must be between 0 and 180')
            super().__setattr__(key, value)
            super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':
            raise AttributeError('Angle_b is calculated automatically')

        else:
            super().__setattr__(key, value)

    def angle_b(self):
        return 180 - self.angle_a

    def __str__(self):
        return f'Rhomb: side A = {self.side_a}, angle A = {self.angle_a}, angle B = {self.angle_b}'



rhombus = Rhomb(10.7, 59.6)
print(rhombus)
