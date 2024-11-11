import math

a = 1
b = 2
h = 0.1
d = 0.001


def func(x, tol=d):
    sum_value = 0
    k = 1
    term = float("inf")
    while abs(term) > tol:
        term = ((-1) ** k * (math.cos(2 * k * x) ** 4)) / (2 * (2 * k))
        sum_value += term
        k += 1
    return sum_value


# Заміна np.arange для генерації значень x
x_values = [a + i * h for i in range(int((b - a) / h) + 1)]
results = [(x, func(x)) for x in x_values]

for x, y in results:
    print(f"x = {x:.1f}, y = {y:.6f}")
