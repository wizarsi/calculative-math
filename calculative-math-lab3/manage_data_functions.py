import math

from calculative_methods import count_simpson_method, count_trapezoidal_method

count_methods = {1: {"name": "Метод Симпсона", "method": count_simpson_method},
                 2: {"name": "Метод Трапеций", "method": count_trapezoidal_method}}
functions = {1: {"name": "-3x^3-5x^2+4x-2", "function": lambda x: -3 * x ** 3 - 5 * x ** 2 + 4 * x - 2},
             2: {"name": "x^3-2x^2-x+1", "function": lambda x: x ** 3 - 2 * x ** 2 - x + 1},
             3: {"name": "sin(2x)", "function": lambda x: math.sin(2 * x)}}

def choose_calculative_method():
    print(f"1. {count_methods[1]['name']}\n2. {count_methods[2]['name']}")
    while 1:
        try:
            method_type = int(input("Введите номер вычислительного метода:"))
            if method_type == 1 or method_type == 2:
                return count_methods[method_type]['method']
        except Exception:
            print("Неправильный ввод")


def choose_equation():
    print(f"1. {functions[1]['name']}\n2. {functions[2]['name']}\n3. {functions[3]['name']}")
    while 1:
        try:
            equation_number = int(input("Введите номер уравнения:"))
            if (1 <= equation_number <= 3): return functions[equation_number]["function"]
        except Exception:
            print("Неправильный ввод")


def choose_borders():
    while 1:
        in_data = input("Введите границы интегрирования a и b, например, 2 10:")
        borders = in_data.strip().split()
        try:
            a = float(borders[0])
            b = float(borders[1])
            if a < b:
                return a, b
            print("a должно быть меньше b")
        except Exception:
            print("Неправильный ввод")


def choose_accuracy():
    while 1:
        in_data = input("Введите точность вычислений:")
        accuracy = in_data.strip().split()
        try:
            return float(accuracy[0])
        except Exception:
            print("Неправильный ввод")
