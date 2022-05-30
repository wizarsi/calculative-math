def delta_y(x, y, h, equation):
    k1 = h * equation(x, y)
    k2 = h * equation(x + h / 2, y + k1 / 2)
    k3 = h * equation(x + h / 2, y + k2 / 2)
    k4 = h * equation(x + h, y + k3)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6


def merge_results_step_1(left_result, right_result):
    left_result.reverse()
    result = left_result[0:len(left_result) - 1] + right_result
    return result


def merge_results_step_4(left_result, right_result):
    left_result = left_result[4:len(left_result)]
    left_result.reverse()
    result = left_result + right_result
    return result


def runge_kutta(a, b, x0, y0, h, equation):
    if h > 0:
        n = int((b - x0) / h)
    else:
        n = int(abs((x0 - a) / h))
    dots = [tuple([x0, y0])]
    y = y0
    x = x0

    for i in range(n):
        y += delta_y(x, y, h, equation)
        x += h
        dots.append(tuple([round(x, 2), round(y, 3)]))
    return dots


def runge_kutta_calculate(a, b, x0, y0, h, accuracy, equation, max_n=5):
    right_result = runge_kutta(a, b, x0, y0, h, equation)
    """left_result = runge_kutta(a, b, x0, y0, -h, equation)
    result = merge_results_step_1(left_result, right_result)"""

    last_y = right_result[len(right_result) - 1][1]
    loop_h = h
    for i in range(max_n):
        loop_h /= 2
        right_result = runge_kutta(a, b, x0, y0, loop_h, equation)
        current_y = right_result[len(right_result) - 1][1]
        if abs((last_y - current_y)) / (2 ** 4 - 1) <= accuracy:
            """left_result = runge_kutta(a, b, x0, y0, -loop_h, equation)
            result = merge_results_step_1(left_result, right_result)"""
            break
        last_y = current_y

    return right_result


def miln(a, b, x0, h, accuracy, equation, dots, derivatives):
    result = dots.copy()
    local_derivatives = derivatives.copy()
    if h > 0:
        n = int((b - x0) / h) + 1
        current_x = x0 + 3 * h
    else:
        n = int(abs((x0 - a) / h) + 4)
        result.reverse()
        local_derivatives.reverse()
        current_x = x0

    for i in range(4, n):
        current_x += h
        y_prediction = result[i - 4][1] + (4 * h / 3) * \
                       (2 * local_derivatives[i - 3] - local_derivatives[i - 2] + 2 * local_derivatives[i - 1])
        local_derivatives.append(equation(current_x, y_prediction))
        y_correction = result[i - 2][1] + (h / 3) * (
                local_derivatives[i - 2] + 4 * local_derivatives[i - 1] + local_derivatives[i])
        while not (abs(y_correction - y_prediction) <= accuracy):
            y_prediction = y_correction
            local_derivatives[i] = equation(current_x, y_prediction)
            y_correction = result[i - 2][1] + (h / 3) * (
                        local_derivatives[i - 2] + 4 * local_derivatives[i - 1] + local_derivatives[i])
        result.append(tuple([round(current_x, 3), y_prediction]))

    return result


def runge_kutta_4_dots(x0, y0, h, equation):
    dots = [tuple([x0, y0])]
    derivatives = [equation(x0, y0)]

    for i in range(1, 4):
        last_x = dots[i - 1][0]
        last_y = dots[i - 1][-1]
        current_y = last_y + delta_y(last_x, last_y, h, equation)
        current_x = last_x + h
        dots.append(tuple([current_x, current_y]))
        derivatives.append(equation(current_x, current_y))
    return dots, derivatives


def miln_calculate(a, b, x0, y0, h, accuracy, equation):
    dots, derivatives = runge_kutta_4_dots(x0, y0, h, equation)

    right_result = miln(a, b, x0, h, accuracy, equation, dots, derivatives)
    left_result = miln(a, b, x0, -h, accuracy, equation, dots, derivatives)
    result = merge_results_step_4(left_result, right_result)
    return result
