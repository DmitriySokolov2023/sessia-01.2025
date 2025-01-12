numbers = []
unique_numbers = []  # Список для уникальных значений

# Запрашиваем у пользователя четыре целых числа
for i in range(4):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

# Ищем третье по величине число
# Добавляем только уникальные числа
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Проверяем, есть ли третье по величине число
if len(unique_numbers) < 3:
    print("Третьего по величине числа не существует.")
else:
    # Сортируем уникальные числа по возрастанию
    for i in range(len(unique_numbers)):
        for j in range(len(unique_numbers) - 1):
            if unique_numbers[j] > unique_numbers[j + 1]:
                unique_numbers[j], unique_numbers[j + 1] = unique_numbers[j + 1], unique_numbers[j]
         
    
    # Третье по величине число находится на индексе 2
    print("Третье по величине число:", unique_numbers[2])