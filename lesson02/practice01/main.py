class Square:
    a = 0

    def __init__(self, a):
        self.a = a

    def calculate_the_area(self):
        print('Area of square is', (self.a * self.a))

    def calculate_the_circumference(self):
        print('Circumference of square is', (4 * self.a))

if __name__ == '__main__':
    square = Square(5)
    square.calculate_the_area()
    square.calculate_the_circumference()
