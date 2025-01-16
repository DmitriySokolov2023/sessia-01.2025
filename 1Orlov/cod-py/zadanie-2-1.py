array = [1, 2, 3, 4, 5,6,7,8,9,10]

print("Исходный массив: ", end=" ")
for i in range(len(array)):
    print(array[i], end=" ")
print()

n = len(array)
for i in range(n //2):
    temp = array[i]
    array[i] = array[n - i - 1]
    array[n - i - 1] = temp

print("Обратный массив: ", end=" ")
for i in range(len(array)):
    print(array[i], end=" ")
print()