from data import get_data
from calculation import runge_kutta_calculate, miln_calculate
import matplotlib.pyplot as plt
import pandas as pd


def plot_chart(coordinates_runge, coordinates_milan, true_solve, x0, y0):
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
    plt.plot([dot[0] for dot in true_solve], [dot[1] for dot in true_solve], color='b',
             label="Точное решение")
    plt.legend()
    plt.show()


def print_table(dots, method_name, true_solve):
    print(f"Результат для {method_name}:")
    result_table = pd.DataFrame(
        {'x': [dot[0] for dot in dots], 'y': [(dot[1]) for dot in dots], 'true': [dot[1] for dot in true_solve]})
    result_table.index.name = '№'
    pd.DataFrame.round
    pd.set_option('display.max_rows', 150)

    print(result_table)


if __name__ == '__main__':
    data = get_data()
    a, b, x0, y0, h, accuracy, equation1, equation2, equation3 = data["a"], data["b"], data["x0"], data["y0"] \
        , data["h"], data["accuracy"], data["equation1"], data["equation2"], data["equation3"]
    result1 = runge_kutta_calculate(a, b, x0, y0, h, accuracy, equation1)
    print_table(result1, "Метод Рунге-Кутта 4- го порядка",
                [tuple([dot[0], equation2(dot[0], equation3(x0, y0))]) for dot in result1])
    result2 = miln_calculate(a, b, x0, y0, h, accuracy, equation1)
    true_solve = [tuple([dot[0], equation2(dot[0], equation3(x0, y0))]) for dot in result2]
    print_table(result2, "Метод Милна",
                true_solve)
    plot_chart(result1, result2, true_solve, x0, y0)
