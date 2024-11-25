matrix = [
    [0, 2, -2, 89, 21],
    [-1, -4, 36, 41, 71],
    [56, 93, 51, -2, -51],
    [1, 3, -8, 0, 9],
    [23, 41, 5, 8, -2],
]


def bubble_sort_columns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        for i in range(rows - 1):
            for j in range(rows - i - 1):
                if matrix[j][col] < matrix[j + 1][col]:
                    matrix[j][col], matrix[j + 1][col] = (
                        matrix[j + 1][col],
                        matrix[j][col],
                    )


def geometric_mean_above_diagonal(matrix):
    rows = len(matrix)
    geometric_means = []

    for i in range(rows):
        product = 1
        count = 0
        for j in range(i + 1, len(matrix[i])):
            if matrix[i][j] > 0:
                product *= matrix[i][j]
                count += 1
        if count > 0:
            geometric_means.append(product ** (1 / count))
        else:
            geometric_means.append(0)
    return geometric_means


def sum_geometric_means(geo_means):
    return sum(geo_means)


print("Оригінальна матриця:")
for row in matrix:
    print(row)

bubble_sort_columns(matrix)

print("\nМатриця після сортування стовпців за спаданням:")
for row in matrix:
    print(row)

fi_values = geometric_mean_above_diagonal(matrix)
print(
    "\nСереднє геометричне значення елементів у кожному рядку над головною діагоналлю (fi(aij)):"
)
print(fi_values)

F_sum = sum_geometric_means(fi_values)
print(f"\nСума fi(aij) (F(fi(aij))): {F_sum}")
