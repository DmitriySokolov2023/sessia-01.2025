array = [55,65,23,23,76,98,65,23,87,99]

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