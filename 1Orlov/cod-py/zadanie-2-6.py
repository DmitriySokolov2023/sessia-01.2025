from random import randint

# Вводим размеры массива и количество единиц
N = int(input("Введите количество строк (N): "))
M = int(input("Введите количество столбцов (M): "))
K = int(input("Введите количество единиц (K): "))

# Проверяем, что количество единиц не больше, чем количество элементов в массиве
if K > N * M:
  print("Кол-во единиц превышает кол-во элементов!")
else:
  #Заполняем массив нулями
  A = []
  for i in range(N):
    row = []
    for j in range(M):
      row.append(0)
    A.append(row)
    


#Случайным образом выбираем индексы и если элемент не равен 0, то заменяем на 1, иначе ищем элемент = 0, пока не запишем K единиц 
while K > 0:
  randN = randint(0,N-1)
  randM = randint(0,M-1)
  if A[randN][randM] !=1:
    A[randN][randM] = 1
    K-=1


A_vertical = A #Создал бекап массива, чтобы перевернуть элементы по горизонтали и по вертикали отдельно 

print('Исходный массив: ')
print()
for el in A:
  print(el)
  
print()
print('Новый массив: ')
print()
#Последовательно вывожу строки основного массива в виде рисунка:
for index, el in enumerate(A):
  for sub_el in el:
    if(sub_el == 1):print("*", end=" ")
    else: print(" ", end=" ")
   
  #Создаю зеркало по горизонтали 
  for i in range(N):
    left = 0
    right = M - 1
    while left < right:
        A[i][left], A[i][right] = A[i][right], A[i][left]
        left += 1
        right -= 1  
    
  #Вывожу рядом с каждой строкой её зеркальное отображение в виде рисунка
  for index_mirror, el_mirror in enumerate(A):
    if(index_mirror == index):
      for sub_el_mirror in el_mirror:
            if(sub_el_mirror == 1):print("*", end=" ")
            else: print(" ", end=" ")
      print()
    	
 	

#Тоже самое делаю по вертикали:
      
for index, el in enumerate(A_vertical):
  for sub_el in el:
    if(sub_el == 1):print("*", end=" ")
    else: print(" ", end=" ")
    
  top = 0
  bottom = N - 1
  while top < bottom:
   A_vertical[top], A_vertical[bottom] = A_vertical[bottom], A_vertical[top]
   top += 1
   bottom -= 1 

  #Вывожу рядом с каждой строкой её зеркальное отображение в виде рисунка
  for index_mirror, el_mirror in enumerate(A_vertical):
    if(index_mirror == index):
      for sub_el_mirror in el_mirror:
            if(sub_el_mirror == 1):print("*", end=" ")
            else: print(" ", end=" ")
      print()       
       
			