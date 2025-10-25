import math

class Shape:
    __count = 0

    def __init__(self, length):
        self._length = length
        self._area = 0
        self._boundary = 0
        Shape.__count += 1

    def calculate_area(self):
       pass

    def calculate_boundary(self):
       pass

    @classmethod
    def get_count(cls):
        return Shape.__count

    def __str__(self):
        return f"Area: {self._area:.2f}\nBoundary: {self._boundary:.2f}"

class Square(Shape):
    __count_square = 0
    def __init__(self, length):
        super().__init__(length)
        self.get_count()

    def __str__(self):
        self.calculate_area()
        self.calculate_boundary()
        desc = super().__str__()
        return f"Square stats: {desc}"

    def calculate_area(self):
        self._area = self._length ** 2
        pass
    def calculate_boundary(self):
        self._boundary = self._length * 4
        pass
    @classmethod
    def get_count(cls):
        Square.__count_square += 1
        print(Square.__count_square)

class Circle(Shape):
    __count_circle = 0
    def __init__(self, length):
        super().__init__(length)
        self.get_count()

    def __str__(self):
        self.calculate_area()
        self.calculate_boundary()
        desc = super().__str__()
        return f"Circle stats: {desc}"

    def calculate_area(self):
        self._area = math.pi * self._length ** 2
        pass
    def calculate_boundary(self):
        self._boundary = self._length * 2 * math.pi
        pass

    @classmethod
    def get_count(cls):
        Circle.__count_circle += 1
        print(Circle.__count_circle)

class Triangle(Shape):
    __count_triangle = 0
    def __init__(self, length):
        super().__init__(length)
        self.get_count()

    def __str__(self):
        self.calculate_area()
        self.calculate_boundary()
        desc = super().__str__()
        return f"Circle stats: {desc}"

    def calculate_area(self):
        self._area = 0.5 * self._length * (self._length * math.sqrt(3)/2)
        pass
    def calculate_boundary(self):
        self._boundary = self._length * 3
        pass

    @classmethod
    def get_count(cls):
        Triangle.__count_triangle += 1
        print(Triangle.__count_triangle)


option = input("Choose s, t, c: ").lower()

if  option == "c":
    size = Circle(int(input("Enter the radius of the circle: ")))
    print(size)
elif option == "s":
    size = Square(int(input("Enter the length of the sides: ")))
    print(size)
else:
    size = Triangle(int(input("Enter the length of the sides: ")))
    print(size)