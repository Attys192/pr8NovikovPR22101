class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]
    def is_triangle(self):

        for side in self.sides:
            if not isinstance(side, (int, float)):
                return "Нужно вводить только числа!"


        for side in self.sides:
            if side <= 0:
                return "С отрицательными числами ничего не выйдет!"


        for i in range(3):
            if self.sides[i] >= sum(self.sides) - self.sides[i]:
                return "Жаль, но из этого треугольник не сделать."

        return "Ура, можно построить треугольник!"

triangle1 = TriangleChecker(3, 4, 5)
print(triangle1.is_triangle())  

triangle2 = TriangleChecker(-1, 4, 5)
print(triangle2.is_triangle())  

triangle3 = TriangleChecker(1, 2, "a")
print(triangle3.is_triangle())  

triangle4 = TriangleChecker(1, 2, 3)
print(triangle4.is_triangle())  