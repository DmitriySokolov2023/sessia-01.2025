A = [
    [ 2, -3,  1,  5, -6,  4],
    [-1,  3, -2,  7,  8, -5],
    [ 9, -4,  6, -8,  1,  2],
    [ 7,  5, -3,  4, -2,  6],
    [-8,  1,  2, -7,  3,  5],
    [ 4, -6,  7, -1,  9, -3]
]

n = 6  # Размер матрицы

product_main_diag = 1

for i in range(n):
    if A[i][i] > 0:
        product_main_diag *= A[i][i]
        found_positive = True

# Если положительных чисел нет, устанавливаем 0
if not found_positive:
    product_main_diag = 0

# 2. Найти сумму элементов побочной диагонали
sum_secondary_diag = 0

for i in range(n):
    sum_secondary_diag += A[i][n - 1 - i]

# Вывод результатов
print("Произведение положительных элементов главной диагонали:", product_main_diag)
print("Сумма элементов побочной диагонали:", sum_secondary_diag)