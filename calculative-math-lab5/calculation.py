import math


def lagrange_interpolation(points, x):
    """Интерполяционный многочлен Лагранжа"""
    lx = 0
    n = len(points)
    for i in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if i != j:
                numerator *= x - points[j][0]
                denominator *= points[i][0] - points[j][0]
        lx += points[i][1] * (numerator / denominator)
    return lx


def newton_interpolation(points, x, print_answer = False):
    """Многочлен Ньютона с конечными  разностями"""
    n = len(points)
    h = points[1][0] - points[0][0]
    differences_matrix = [[0] * n for i in range(n)]

    for i in range(n):
        differences_matrix[0][i] = points[i][1]

    for i in range(1, n):
        for j in range(n - i):
            differences_matrix[i][j] = differences_matrix[i - 1][j + 1] - differences_matrix[i - 1][j]

    # Идем с конца интеравла вторая формула Ньютона
    if x > points[int(n / 2)][0]:
        t = (x - points[n - 1][0]) / h
        nx = differences_matrix[0][n - 1]
        for i in range(1, n):
            numerator = t
            for j in range(1, i):
                numerator *= t + j
            numerator *= differences_matrix[i][n - i - 1]
            nx += numerator / math.factorial(i)
    # Идем с начала интеравла первая формула Ньютона
    else:
        x1_index = 0
        for i in range(0, n):
            if points[i][0] >= x:
                x1_index = i - 1
                break

        t = (x - points[x1_index][0]) / h
        nx = differences_matrix[0][x1_index]
        for i in range(1, n):
            numerator = t
            for j in range(1, i):
                numerator *= t - j
            numerator *= differences_matrix[i][x1_index]
            nx += numerator / math.factorial(i)
        if print_answer:
            print(f"Метод Ньютона ход с начала индекс старта: {x1_index}")
            for i in range(n):
                print(differences_matrix[i])
    return nx
