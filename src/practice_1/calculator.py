#Аспекты тестирования:
# - корректность при сложении чисел
# - корректность при вычитании чисел
# - корректность при умножении чисел
# - корректность при делении чисел


class Calculator:

    def add(self, value_left, value_right) -> float:
        return value_left + value_right

    def subtract(self, value_left, value_right) -> float:
        return value_left - value_right

    def multiply(self, value_left, value_right) -> float:
        return value_left * value_right

    def divide(self, value_left, value_right) -> float:
        return value_left / value_right


c1 = Calculator()


