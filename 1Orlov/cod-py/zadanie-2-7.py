import random

# Шаг 1: Создадим полный набор чисел от 0 до 65535 (имитация UInt16)
full_set_sum = 0  # Сумма всех чисел от 0 до 65535
array_sum = 0     # Сумма элементов массива, из которого удалим одно число
array = []        # Массив чисел

# Создаем массив и вычисляем сумму всех чисел от 0 до 65535, исключая одно случайное число
missing_number = random.randint(0, 65535)

# Суммируем все числа от 0 до 65535
for i in range(65536):
    print(i)
    if i != missing_number:
        array.append(i)
        array_sum += i
    full_set_sum += i

# Шаг 2: Определим, какое число не хватает
missing_number_found = full_set_sum - array_sum

# Выводим результат
print(f"Отсутствующее число: {missing_number_found}")