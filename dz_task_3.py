# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 
from random import randint
num = randint(0, 1000)
count = 0
QUANTITY = 10
while count != QUANTITY:
    a = int(input("Введите число от 0 до 1000: "))
    if a != num:
        if a > num:
            count += 1
            print(f"Вы ввели неправильное число, угадываемое число меньше чем ваше,у вас осталось {QUANTITY - count} попыток")
        else:
            count += 1
            print(f"Вы ввели неправильное число, угадываемое число больше чем ваше, у вас осталось {QUANTITY - count} попыток")
    else: 
        print("Вы угадали!")
