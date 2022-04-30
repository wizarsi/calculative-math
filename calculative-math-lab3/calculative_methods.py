# Метод трапеций
def count_trapezoidal_method(function, a, b, accuracy, n=4, max_n=2**20, k=2):
    last_sum = 0

    while n <= max_n:
        sum = function(a) + function(b)
        h = (b - a) / n
        for i in range(1, n):
            sum += 2 * function(a + i * h)
        sum *= (h / 2)
        if last_sum != 0 and abs((last_sum - sum) / (2 ** k - 1)) <= accuracy:
            return sum, n

        n *= 2
        last_sum = sum

# Метод Симпсона
def count_simpson_method(function, a, b, accuracy, n=4, max_n=2**15, k=4):
    last_sum = 0

    while n <= max_n:
        sum = function(a) + function(b)
        h = (b - a) / n
        for i in range(1, n):
            if i % 2 == 0:
                sum += 2 * function(a + i * h)
            else:
                sum += 4 * function(a + i * h)

        sum *= (h / 3)
        if last_sum != 0 and abs((last_sum - sum) / (2 ** k - 1)) <= accuracy:
            return sum, n

        n *= 4
        last_sum = sum
