def substring_search(str, substr):
    str_length = len(str)
    substr_len = len(substr)

    for i in range(str_length - substr_len + 1):  
        match = True
        for j in range(substr_len):  
            if str[i + j] != substr[j]:  
                match = False
                break  
        
        if match:  
            return i 
    
    return -1  


str = input("Введите строку: ")  
substr = input("Введите подстроку для поиска: ")  

index = substring_search(str, substr)  

# Вывод результата
if index != -1:
    print(f"Подстрока найдена на позиции {index}")
else:
    print("Подстрока не найдена")