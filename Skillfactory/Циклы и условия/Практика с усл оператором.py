# Хорошо
# if not seq:
# if seq:

# Плохо
# if len(seq)
# if not len(seq)

# Примеры

# if pozitive_num:  # нет смысла проверять len(pozitive_num)
#    # если список не пустой, печатаем его
#    print("Список положительных чисел равен: ", pozitive_num)
# else:
#    # печатаем, если список оказался пустым
#    print("Список положительных чисел пустой")


# if not password:  # password строка содержащая пароль, введённый пользователем
#    print("Вы забыли ввести пароль! Повторите попытку ещё раз")

# Условие задачи: запишите условие проверки, которое является истинным, когда каждое из чисел А и В нечётное.
A, B = 20, 10
if A % 2 == 1 and B % 2 == 1:
    print('Числа А и B нечетные')
x,  y = 3, 6
if x > 0 and y > 0:
    print("Первая четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")
a = 13
if a == 10:
    print('a равно 10')
elif a < 10:
    print('a меньше 10')
else:
    print('a больше 10')

month = int(input("Введите число месяца"))

if month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
elif month in [12, 1, 2]:
    print("Зима")

wind = int(input())

if 1 <= wind <= 4:
   print("слабый (1)")
elif 5 <= wind <= 10:
   print("умеренный (2)")
elif 11 <= wind <= 18:
   print("сильный (3)")
elif wind >= 19:
   print("ураганный (4)")

login_list = [
   'root',
   'username1', 
   'f0x1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123',
   'f0x1': '13310011'
}

username = input('Введите логин:\n')

if username in login_list:
   password = input('Введите пароль:\n')
   if password_list[username] == password:
       print('Вы успешно вошли в систему')
   else:
       print('Отказано в доступе')
else:
   print('Такого пользователя не существует')

A = int(input('Введите первое число\n'))
B = int(input('Введите второе число\n'))
C = int(input('Введите третье число\n'))

if ((A < 45) and (B >= 45) and (C >=45)) or \
    ((A >= 45) and (B < 45) and (C >=45)) or \
    ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')

A = int(input('Введите число\n'))

if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("Число не принадлежит интервалу")
else:
    print("Число принадлежит интервалу")

n = 15
first_digit = n // 10
second_digit = n % 10

print((first_digit == 5) or (second_digit == 5))

list_ = [-5, 2, 4, 8, 12, -7, 5]

print(len(list_) == len(set(list_)))

num = 12345678

print(str(num) == str(num)[::-1])
