
N = [] 

for i in range(1,21):
    N.append(i)

# Создаем пустой массив Y
Y = [0] * 20 

# Записываем квадраты чисел из N в Y
for i in range(20):
    Y[i] = N[i] * N[i] 


print("Массив N:")
for i in range(20):
    print(N[i], end=" ")
print()

print("Массив Y (квадраты чисел из N):")
for i in range(20):
    print(Y[i], end=" ")
print()