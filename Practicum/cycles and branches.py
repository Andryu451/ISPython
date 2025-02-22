bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']
bremen_musicians.append("Атаманша")
for musician in bremen_musicians:

    # Каждый элемент списка bremen_musicians 
    # по очереди будет передан в переменную musician
    # и напечатан
    print(musician)


# Здесь может быть какой-то код, который выполнится
# только после того, как цикл закончит работу


around_zero = range(-3, 3)

# Вместо списка в цикл передаётся переменная around_zero, 
# в ней хранится range() от -3 до 3
for i in around_zero:
    # Перебрать все числа в диапазоне от -3 до 3 и напечатать их:
    print(i)
# Будет напечатано
# -3
# -2
# -1
# 0
# 1
# 2

countdown_str = ""
for i in reversed(range(0,11)):
    countdown_str = countdown_str + str(i) + ", "

countdown_str = countdown_str + "поехали!"
print(countdown_str)

for current_hour in range(24):
    if current_hour < 12:
        print('Доброе утро!')
    if current_hour >= 12:
        print("Добрый день!")

for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    
    if current_hour >= 6 and current_hour <= 11 :  
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:  
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:                       
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')

# Добавьте новые условия в elif и else
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        # напишите ваш код здесь
        print("У вас", messages_count, "новое сообщение")
    elif messages_count >=2 and messages_count <= 4:
        print("У вас", messages_count, "новых сообщения")
    elif messages_count >4 and messages_count <= 21:
        print("У вас", messages_count, "новых сообщений")

new_mail = 0
if new_mail > 0:
    print('Пришло письмо, не пропусти!')
else:
    print('Никто не пишет.')
# Тут код, отсчитывающий минуту

# И снова проверим почту
if new_mail > 0:
    print('Пришло письмо, не пропусти!')
else:
    print('Никто не пишет.')
# Тут код, отсчитывающий минуту

# И снова
if new_mail > 0:
    print('Пришло письмо, не пропусти!')
else:
    print('Никто не пишет.')
# Тут код, отсчитывающий минуту

# За это время пришло письмо:
new_mail = 1
# И снова проверка
if new_mail > 0:
    print('Пришло письмо, не пропусти!')
else:
    print('Никто не пишет.')

#Itproger
def func_test(word):#word - параметры
    print(word, end="")#end - отсутствие переноса на новую строку
    print("!")

func_test("Hello")
func_test(5.6)
