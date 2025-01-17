B = [
    [ 1, -3,  4,  5,  2,  3],
    [ 2,  1, -2,  3,  4, -1],
    [-1,  3,  0,  6, -3,  2],
    [ 5, -1,  2,  3,  1,  0],
    [ 4,  2,  3, -1,  1,  2],
    [-3,  0,  1,  2, -2,  5]
]

print('Исходная матрица: ')
for el in B:
    print(el)
    
K = 6
X = []

n = 6 #Размерность

# Перебираем элементы ниже главной диагонали, т.е i > j - всегда, начинаем с i=1, j=0
for i in range(1, n):  
    for j in range(i): 
        if B[i][j] <= K and B[i][j] > i + j:
            X.append(B[i][j])  

print("Массив X:", X)