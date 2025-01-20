import random
import time

# 1 Сортировка Пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 2 Сортировка - Прямое включение
def in_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3 Сортировка - Прямой выбор
def sel_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 4 Сортировка - Шейкерная
def shaker_sort(arr):
    n = len(arr)
    start, end = 0, n - 1
    while start < end:
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        end -= 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        start += 1

# 5. Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# 6. Сортировка Хоара
def fast_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return fast_sort(left) + middle + fast_sort(right)

# Подсчет времени каждой из сортировок
def timer(sort, arr):
    start_time = time.time()
    sort(arr)
    end_time = time.time()
    return end_time - start_time

def rnd_array(size):
    arr= []
    for _ in range(size):
        arr.append(random.randint(0,100)) # Заполнение массива рандомными числами от 1 до 100 (размерностью size)



def main():
    size = 1000 # Размерность массива для теста
    GREEN = "\033[32m" #Цвет в консоли (выделить время сортировки)
    RESET = "\033[0m" # Сброс цвета в конце строки
    
    # Массив для удобного вывода результатов в консоль
    sorts = [{"label":"Сортировка Пузырьком","sort":bubble_sort},
             {"label":"Сортировка Прямого включения","sort":in_sort},
             {"label":"Сортировка Прямого выбора","sort":sel_sort},
             {"label":"Шейкерная сортировка","sort":shaker_sort},
             {"label":"Сортировка методом Шелла","sort":shell_sort},
             {"label":"Сортировка методом Хоара","sort":fast_sort}, ]

    #Пробегаемся по массиву и вызываем нужные функции, форматируем текст
    for sort in sorts:
        arr = rnd_array(size)
        print(f"{sort['label']} заняла:{GREEN} {timer(sort["sort"], arr):.4f}{RESET}")

main()