import matplotlib.pyplot as plt
import numpy as np

def get_derivative(function, coordinate):
    a = 0.000000001
    return (function(a + coordinate) - function(coordinate - a)) / (2 * a)


def solve_simple_iteration_method(func, a, b, accuracy):
    derivative_a = get_derivative(func, a)
    derivative_b = get_derivative(func, b)
    my_lambda = -(1 / derivative_a) if (derivative_b < derivative_a) else -(1 / derivative_b)
    print(f"Derivative at a: {derivative_a}\nDerivative at b: {derivative_b}\n")
    fi_function = lambda s: my_lambda * func(s) + s
    fi_derivative_a = get_derivative(fi_function, a)
    fi_derivative_b = get_derivative(fi_function, b)
    message = ""
    if abs(fi_derivative_a) <= 1 and abs(fi_derivative_b) <= 1:
        message = "The sufficient condition for convergence is satisfied"
    print(message)
    current = a
    previous = fi_function(a)

    steps = 0
    print("xi     xi+1     f(xi)")
    while abs(previous - current) > accuracy:
        previous = current
        current = fi_function(current)
        print(f'{previous:^10.3f}     {current:^10.3f}     {func(previous):^10.6f}')
        steps += 1
        if (steps > 200):
            print("Failed to count:(")


    print(f"x = {current},f(x) = {func(current)} ,count iterations = {steps}")

    return current, steps


def solve_newton_method(func, a, b, accuracy):
    if func(a) * func(b) > 0:
        print("There are no roots in this area")
        return
    print("xi     xi+1     f(xi)")
    steps = 0
    previous = b
    h = func(previous) / get_derivative(func, previous)
    current = previous - h
    while 1:
        steps += 1
        previous = current
        current = previous - func(previous) / get_derivative(func, previous)
        print(f'{previous:^10.3f}     {current:^10.3f}     {func(previous):^10.6f}')
        if abs(previous - current) <= accuracy:
            break

    print(f"x = {current},f(x) = {func(current)} ,count iterations = {steps}")
    return current, steps


def solve_system_iteration_method(func1, func2, approximation1, approximation2, accuracy):
    previous1, previous2 = approximation1, approximation2
    steps = 0
    while 1:
        current1,current2 = func1(previous1, previous2), func2(previous1, previous2)
        if abs(current1 - previous1) < accuracy or abs(current2 - previous2) < accuracy:
            break
        steps += 1
        previous1, previous2 = current1, current2
    print(f"x = {current1}, y = {current2}, f(x,y) = {func1(current1,current2)},count iterations = {steps}")
    return steps, current1, current2

def show_graph(func, min_x=-12, max_x=12, min_y=-12, max_y=12, interval=1):
    x = np.linspace(min_x, max_x, 500)
    graph = plt.figure()
    canvas = graph.add_subplot(1, 1, 1)
    canvas.spines['left'].set_position('center')
    canvas.spines['bottom'].set_position('center')
    canvas.xaxis.set_ticks_position('bottom')
    canvas.yaxis.set_ticks_position('left')

    canvas.plot(x, func(x), "r")
    canvas.set(xlim=(min_x, max_x), xticks=np.arange(min_x, max_x, interval),
           ylim=(min_y, max_y), yticks=np.arange(min_y, max_y, interval))
    plt.show()

