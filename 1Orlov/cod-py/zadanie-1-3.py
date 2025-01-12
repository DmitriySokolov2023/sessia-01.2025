numbers = []
for i in range(4):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

# Проверяем наличие одинаковых чисел
has_duplicates = False

for i in range(4):
    for j in range(i + 1, 4):
        if numbers[i] == numbers[j]:
            has_duplicates = True
            break


# Вывод результата
if has_duplicates:
    print("Среди введенных чисел есть одинаковые.")
else:
    print("Все введенные числа различны.")