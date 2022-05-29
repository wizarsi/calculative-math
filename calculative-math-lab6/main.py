from data import get_data
from calculation import runge_kutta_calculate, miln_calculate
import matplotlib.pyplot as plt
import pandas as pd


def plot_chart(coordinates_runge, coordinates_milan, x0, y0):
    gr = plt.gca()
    gr.spines['left'].set_position('zero')
    gr.spines['top'].set_color('none')
    gr.spines['bottom'].set_position('zero')
    gr.spines['right'].set_color('none')
    plt.plot([dot[0] for dot in coordinates_runge], [dot[1] for dot in coordinates_runge], color='r',
             label="Метод Рунге-Кутта")
    plt.plot([dot[0] for dot in coordinates_milan], [dot[1] for dot in coordinates_milan], color='g',
             label="Метод Малана")
    plt.plot(x0, y0, marker="D", color="b", label="Начальная точка")
    plt.legend()
    plt.show()


def print_table(dots, method_name):
    print(f"Результат для {method_name}:")
    result_table = pd.DataFrame({'x': [dot[0] for dot in dots], 'y': [dot[1] for dot in dots]})
    result_table.index.name = '№'
    #pd.set_option('display.max_rows', None)

    print(result_table)


if __name__ == '__main__':
    data = get_data()
    a, b, x0, y0, h, accuracy, equation = data["a"], data["b"], data["x0"], data["y0"] \
        , data["h"], data["accuracy"], data["equation"]
    result1 = runge_kutta_calculate(a, b, x0, y0, h, accuracy, equation)
    print_table(result1, "Метод Рунге-Кутта 4- го порядка")
    result2 = miln_calculate(a, b, x0, y0, h, accuracy, equation)
    print_table(result2, "Метод Милна")
    plot_chart(result1, result2, x0, y0)
