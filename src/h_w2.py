#Аспект тестирования корректность работы ф-ии с разными входными данными и корректность нахождения среднего значения

def average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count


#Аспект тестирования корректность работы ф-ии с разными входными данными и нахождения фактриала числа
def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(3))