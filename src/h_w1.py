from math import sqrt


# def input_param(text):
#     num = 0

    # while True:
    #     try:
    #         num = float(input(text))
    #         return num
    #     except ValueError:
    #         print("Ошибка ввода данных! Введите чиловое значение.")


def QuadraticEquation():

    a = float(input('Введите коэффициенты  "a"  для уравнения ax^2 + bx + c = 0 >>> '))
    b = float(input('Введите коэффициенты  "b"  для уравнения ax^2 + bx + c = 0 >>> '))
    c = float(input('Введите коэффициенты  "c"  для уравнения ax^2 + bx + c = 0 >>> '))

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2*a)
        root2 = (-b - sqrt(discriminant)) / (2*a)
        print(f'Корни уравнения: ', root1, 'и', root2)

    elif discriminant == 0:
        root = -b / (2*a)
        print(f'Единственный корень уравнения: ', root)

    else:
        print('У уравнения нет действительных корней')


# QuadraticEquation()

def TriangleArea():

    a = float(input('Введите длину стороны треугольника "a" >>> '))
    b = float(input('Введите длину стороны треугольника "b" >>> '))
    c = float(input('Введите длину стороны треугольника "c" >>> '))

    if a > 0 and b > 0 and c > 0:
        if ((a + b) > c) or ((a + c) > b) or ((b + c) > a):
            s = (a + b + c) / 2
            area = sqrt(s * (s - a) * (s - b) * (s - c))
            print(f'Площадь треугольника: ', area)
    else:
        print('Условия существования треугольника не соблюдены')


# TriangleArea()


def TemperatureConversion():

    choice = float(input("""Выберите опцию: 
    1. Конвертировать Цельсий в Фаренгейт
    2. Конвертировать Фаренгейт в Цельсий
    >>> """))

    if choice == 1:
        celsius = float(input('Введите температуру в градусах Цельсия:'))
        fahrenheit = (celsius * 9 / 5) + 32
        print('Температура в градусах Фаренгейта:', fahrenheit)

    elif choice == 2:
        fahrenheit = float(input('Введите температуру в градусах Фаренгейта:'))
        celsius = 5/9 * (fahrenheit - 32)
        print('Температура в градусах Цельсия: ', celsius)


    else:
        print('Неправильный выбор')


# TemperatureConversion()


