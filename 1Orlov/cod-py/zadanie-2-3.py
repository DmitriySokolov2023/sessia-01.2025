from random import randint  

numbers = []
for i in range(4):
    numbers.append(randint(1,5))

print(numbers)

max = numbers[0]
min = numbers[0]

for num in numbers:
    if num > max:
        max = num
    if num < min:
        min = num

count_max = 0
count_min = 0

#Ищем кол-во повторений
for num in numbers:
    if(num == max):
        count_max+=1
    if(num == min):
        count_min+=1

print('Максимальное число: ',max)
print('Минимальное число: ', min)
print('Кол-во максимальных чисел: ', count_max)
print('Кол-во минимальных чисел: ', count_min)
