import math


def get_сauchy_equation(task_number):
    if task_number == 1:
        return lambda x, y: x ** 2 + y, lambda c, x: c * math.e ** x - x ** 2 - 2 * x - 2 \
            , lambda x, y: (y + x ** 2 + 2 * x + 2) / (math.e ** x)
    if task_number == 2:
        return lambda x, y: y + math.cos(x), lambda x, c: math.sin(x) * 0.5 - math.sin(x) * 0.5 + c * math.e ** x, \
               lambda x, y: (-math.sin(x) * 0.5 + math.sin(x) * 0.5 + y) / (math.e ** x)
    if task_number == 3:
        return lambda x, y: (2 * y) + x ** 2, lambda x, c: c * math.e ** (2 * x) - (x ** 2) * 0.5 - x / 2 - 1 / 4, \
               lambda x, y: (y + (x ** 2) * 0.5 + x / 2 + 1 / 4) / (math.e ** (2 * x))


def enter_value(text):
    while True:
        try:
            x = float(input(f"Введите {text}: "))
            return x
        except:
            print("Некоректный ввод")


def get_data():
    while True:
        try:
            print("1 y' = x^2 + y\n2 y' = y + cos(x)\n3 y' = (2 * y) + x^2")
            task_number = int(input("Выберите задачу Коши: "))
            if task_number >= 1 and task_number <= 3:
                equation1, equation2, equation3 = get_сauchy_equation(task_number)
                break
            else:
                print("Нет такой задачи")

        except:
            print("Некорректный ввод")
    x0 = enter_value("x0")
    y0 = enter_value("y0")
    while True:
        try:
            borders = tuple(map(float, input("Введите границы интервала a и b: ").strip().split()))

            if borders[0] < borders[1]:
                break
            else:
                print("Левая граница должна быть меньше правой")
        except:
            print("Некорректный ввод")
    h = -1
    while h <= 0:
        h = enter_value("шаг h")
        if h <= 0:
            print("h должно быть >0")
    a = -1
    while a <= 0:
        a = enter_value("точность, например, 0.01")
        if a <= 0:
            print("a должно быть >0")

    return {"a": borders[0], "b": borders[1], "x0": x0, "y0": y0, "h": h, "accuracy": a, "equation1": equation1,
            "equation2": equation2, "equation3": equation3}
