# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt


class Side:
    @staticmethod
    def width(a1, b1):
        return sqrt(sum(tuple(map(lambda a1, b1: (b1 - a1) ** 2, a1, b1))))


class Triangle(Side):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        return (self.width(self._a, self._b) +
                self.width(self._b, self._c) +
                self.width(self._a, self._c)) / 2

    def area(self):
        p = self.perimeter()
        ab = self.width(self._a, self._b)
        bc = self.width(self._b, self._c)
        ac = self.width(self._a, self._c)
        return sqrt(p * (p - ab) * (p - bc) * (p - ac))


A1, A2, A3 = (5, 10), (10, 12), (5, -15)

ABC = Triangle(A1, A2, A3)

print("\n  -=  Задание 1  =-")
print('В треугольнике со сторонами:')
print(f'AB = {round(ABC.width(A1, A2),2)}, '
      f'BC = {round(ABC.width(A2, A3),2)}, '
      f'AC = {round(ABC.width(A1, A3),2)}')
print(f'Площадь: {round(ABC.area(), 2)} кв. ед')
print(f'Периметр: {round(2 * ABC.perimeter(), 2)} ед')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze(Side):
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def is_equilateral(self):
        return ((self.width(self._a, self._c) == self.width(self._b, self._d) and   # равны диагонали
                ((self.width(self._a, self._b) == self.width(self._c, self._d)) or   # и одна из пар
                (self.width(self._a, self._b) == self.width(self._c, self._d)))))    # противоположных сторон

    def is_trapeze(self):
        return (((self._b[1] - self._a[1]) / (self._b[0] - self._a[0]) ==
                (self._d[1] - self._c[1]) / (self._d[0] - self._c[0])) or      # одна из пар
                ((self._d[1] - self._a[1]) / (self._d[0] - self._a[0]) ==      # противоположных сторон
                (self._c[1] - self._b[1]) / (self._c[0] - self._b[0])))        # параллельны

    def perimeter(self):
        return (self.width(self._a, self._b) + self.width(self._b, self._c) +
                self.width(self._c, self._d) + self.width(self._a, self._d))

    def area(self):
        h = sqrt(self.width(self._a, self._b) ** 2 -
                 ((self.width(self._a, self._d) - self.width(self._b, self._c)) / 2)**2)

        return (self.width(self._b, self._c) + self.width(self._a, self._d)) * h / 2


#trap = Trapeze((-7, 4), (-5, 6), (6, 6), (8, 5))
trap = Trapeze((-7, 4), (-5, 6), (5, 6), (7, 4))

print("\n  -=  Задание 2  =-")

if trap.is_trapeze():
    print(f"Четырехугольник с вершинами\nA{trap._a}, B{trap._b}, C{trap._c}, D{trap._d}\nявляется трапецией")
    if trap.is_equilateral():
        print(f'Эта трапеция является равнобокой!')
    else:
        print(f'Эта трапеция не является равнобокой!')

    print(f"Периметр трапеции: {round(trap.perimeter(), 2)}")
    print(f"Площадь трапеции: {round(trap.area(), 2)}")
else:
    print(f"Четырехугольник с вершинами\nA{trap._a}, B{trap._b}, C{trap._c}, D{trap._d}\nне является трапецией")
