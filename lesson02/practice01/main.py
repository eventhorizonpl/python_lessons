class Rectangle:
    a = 0

    def __init__(self, a):
        self.a = a

    def calculate_the_area(self):
        print('Area of rectangle is', (self.a * self.a))

    def calculate_the_circumference(self):
        print('Circumference of rectangle is', (4 * self.a))

if __name__ == '__main__':
    rectangle = Rectangle(5)
    rectangle.calculate_the_area()
    rectangle.calculate_the_circumference()
