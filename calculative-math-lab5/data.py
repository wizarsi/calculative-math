import numpy as np


def get_file_data():
    data = []
    input_path = "data.txt"

    with open(input_path, encoding="UTF-8") as file:
        try:
            for point in file:
                current_point = tuple(map(float, point.strip().split()))
                if len(current_point) != 2:
                    raise Exception
                data.append(current_point)
        except:
            return None
    return data


def get_console_data():
    data = []
    try:
        string_count = int(input("Введите количество точек: "))
        print("Введите координаты через пробел построчно")
        for i in range(string_count):
            point = input()
            current_point = tuple(map(float, point.strip().split()))
            if len(current_point) != 2:
                raise ValueError
            data.append(current_point)
    except:
        return None

    return data


def get_data():
    print("1 - считать из файла\n2 - считать посредством ввода с консоли")
    while True:
        try:
            get_data_type = int(input("Введите тип считываения: "))
            if get_data_type == 1:
                in_data = get_file_data()
            elif get_data_type == 2:
                in_data = get_console_data()
            else:
                print("Нет такого типа считываения")
            if in_data != None:
                break
            else:
                print("Не получилось корректно считать данные")
        except:
            print("Повторите тип счтывания данных")
    return in_data


def get_function(func_number):
    if func_number == 1:
        return lambda x: x ** 3
    if func_number == 2:
        return lambda x: np.cos(x)
    if func_number == 3:
        return lambda x: (2 * x) ** 0.5


def calc_dots(func, a, b, n):
    result = []
    step = (b - a) / (n - 1)
    for i in range(n):
        result.append((a, func(a)))
        a += step
    return result


def get_dots_from_func():
    while True:
        try:
            print("1 x^3\n2 cos(x)\n3 (2 * x)^0.5")
            func_number = int(input("Выберите функцию: "))
            if func_number >= 1 and func_number <= 3:
                func = get_function(func_number)
                break
            else:
                print("Нет такой функции")

        except:
            print("Некорректный ввод")
    while True:
        try:
            borders = tuple(map(float, input("Введите границы интервала: ").strip().split()))

            if borders[0] < borders[1]:
                break
            else:
                print("Левая граница должна быть меньше правой")
        except:
            print("Некорректный ввод")

    while True:
        try:
            n = int(input("Введите число разбиений интервала: "))
            if n < 2:
                print("Количество узлов должно быть больше 2")
            else:
                break
        except:
            print("Некорректный ввод")
    return calc_dots(func, borders[0], borders[1], n)
