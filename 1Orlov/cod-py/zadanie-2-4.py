B = [
    [ 2, -3,  1],
    [-1,  3, -2],
    [ 9, 0,  6],
    [ 7,  0, -3],
    [-8,  0,  2],
    [ 4, 0,  7],
    [ 0, 0,  9]
]
print('Исходная матрица: ')
for el in B:
    print(el)
n = 7  
m = 3  


sum_pos = 0    
count_otr = 0  

for i in range(n):
    for j in range(m):
        if B[i][j] > 0:
            sum_pos += B[i][j] 
        elif B[i][j] < 0:
            count_otr += 1  
        else:  # Если элемент равен 0
            B[i][j] = 1  # Заменяем 0 на 1

# Выводим результаты
print("Сумма положительных элементов:", sum_pos)
print("Количество отрицательных элементов:", count_otr)
print("Измененная матрица B: ")
for el in B:
    print(el)