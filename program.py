from math import sqrt

message = '''Добро пожаловать в самую лучшую программу для вычисления
квадратного корня из заданного числа'''


def Calculate_Square_Root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        pass
    else:
        message = f'''Мы вычислили корень квадратный из введенного вами числа.
        Это будет: {Calculate_Square_Root(your_number)}'''
        return message


print(message)
calc(25.5)
