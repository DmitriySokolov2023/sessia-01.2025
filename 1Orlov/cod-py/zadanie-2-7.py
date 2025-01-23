import random


sum_all_num = 0  
arr_sum = 0 
arr = []    
GREEN = "\033[32m" #Цвет в консоли (выделить время сортировки)
RESET = "\033[0m" # Сброс цвета в конце строки

# Определяем число для пропуска
missing_number = random.randint(0, 65535)

# Сумма чисел от 0 до 65535
for i in range(65536):
    if i != missing_number:
        arr.append(i)
        arr_sum += i
    sum_all_num += i

# Вычитая из суммы всех элементов, сумму без одного элемента - узнаем значение этого элемента
not_found = sum_all_num - arr_sum

# Вывод
print("Отсутствующее число:",GREEN, not_found,RESET) #GREEN и RESET определяют какой элемент нужно закрасить зеленым (отсутствующее число)