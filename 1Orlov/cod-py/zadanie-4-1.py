def linear_search(arr, target):
    for i in range(len(arr)):  
        if arr[i] == target:  
            return i 
    return -1  

array = [76, 546, 56, 56, 111, 23, 8] 
element = int(input("Введите число для поиска: "))  

# Вызываем функцию поиска
index = linear_search(array, element)

# Вывод результата
if index != -1:
    print(f"Элемент {element} найден в массиве на позиции {index}")
else:
    print(f"Элемент {element} не найден в массиве")