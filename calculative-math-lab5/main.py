from data import get_data, get_dots_from_func
from calculation import lagrange_interpolation, newton_interpolation
import numpy as np
import matplotlib.pyplot as plt


def set_interpolation_calc():
    while True:
        try:
            print("1 Многочлен Лагранжа\n2 Многочлен Ньютона с конечными  разностями")
            interpolation_type = int(input("Введите метод интерполяции: "))
            if not (interpolation_type >= 1 and interpolation_type <= 2):
                raise Exception
            else:
                break
        except:
            print("Некорректный ввод")

    while True:
        try:
            print("1 Ваши точки\n2 Точки из функции")
            source_type = int(input("Введите источник данных: "))
            if not (source_type >= 1 and source_type <= 2):
                raise Exception
            else:
                break
        except:
            print("Некорректный ввод")
    return interpolation_type, source_type


def enter_x_arg():
    while True:
        try:
            x = float(input("Введите значение аргумена функции x: "))
            return x
        except:
            print("Некоректный ввод")


def plot_chart(x, y, abscissa, ordinates, answer):
    gr = plt.gca()
    gr.spines['left'].set_position('zero')
    gr.spines['top'].set_color('none')
    gr.spines['bottom'].set_position('zero')
    gr.spines['right'].set_color('none')
    plt.plot(abscissa, ordinates, color='r', label="Интерполирующая функция")
    plt.plot(x, y, 'o', color='g', label="Входной набор точек")
    plt.plot(answer[0], answer[1], marker="D", color="b", label="Результат интерполяции")
    gr.plot(1, 0, marker=">", color='k', transform=gr.get_yaxis_transform(), clip_on=False)
    gr.plot(0, 1, marker="^", color='k', transform=gr.get_xaxis_transform(), clip_on=False)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    interpolation_type, source_type = set_interpolation_calc()
    if source_type == 1:
        dots = get_data()
    elif source_type == 2:
        dots = get_dots_from_func()
    dots.sort(key=lambda x: x[0])

    n = len(dots)
    points_x = [coord[0] for coord in dots]
    points_y = [coord[1] for coord in dots]
    x = enter_x_arg()
    x_coords = np.linspace(dots[0][0], dots[n - 1][0], 80)

    if interpolation_type == 1:
        result = lagrange_interpolation(dots, x)
        y_coords = [lagrange_interpolation(dots, x_coord) for x_coord in x_coords]
    elif interpolation_type == 2:
        result = newton_interpolation(dots, x)
        y_coords = [newton_interpolation(dots, x_coord) for x_coord in x_coords]

    plot_chart(points_x, points_y, x_coords, y_coords, [x, result])

    print(f"Результат интерполяции: {result}")
