#Аспекты тестирования:
# - корректность работы с различными входными данными
# - корректность при сложении элементов массива
# - корректность при умножении элементов массива
# - корректность при вычислении среднего значения

class Array:

    def __init__(self, *args):
        self.array = args

    def sum(self) -> float:
        summa = 0

        for i in self.array:
            summa += i

        return summa

    def multiply(self) -> float:
        multiply = 1

        for i in self.array:
            multiply *= i

        return multiply

    def average(self) -> float:
        return self.sum() / len(self.array)


a1 = Array(1, 2, 2)

print(a1.sum())
print((a1.multiply()))
print((a1.average()))


