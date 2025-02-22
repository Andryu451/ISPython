import math
def get_mul_func(m):
    nonlocal_m = m
    def local_mul(n):
        return n*nonlocal_m
    return local_mul

two_mul = get_mul_func(5)
print(two_mul(7))


def funcshn(o, u, s):
    res = o+u+s
    return res
s = 10
print(funcshn(13, 25, s))



#плохой стиль написания кода
PI = 3.14
def area_cyrcle(r):
    global PI
    print("Число PI выведенное из локальной области видимости до изменения", PI) # становится локальной. при global PI нелокальная

    PI = 3.1415927#изменение глобальной переменной
    print("Число PI выведенное из локальной области видимости после изменения", PI)
    return PI *(r**2)

print("Число PI выведенное из глобальной области видимости до вызова функции", PI)
print(float(area_cyrcle(10)))
print("Число PI выведенное из глобальной области видимости после вызова функции", PI)

#хороший стиль написания кода
PI = 3.14
def area_cyrcle(r):
    return PI *(r**2)

print("Число PI выведенное из глобальной области видимости до вызова функции", PI)
print(float(area_cyrcle(10)))
print("Число PI выведенное из глобальной области видимости после вызова функции", PI)




def brand(**brands):
    for x, y in brands.items():
        print(x, ":", y)
brand(A = "Apple", M="Microsoft", S = "Samsung", T = "Tecno")

i = 1
def foo():
    i = 5
    print(i, "local in foo()")
print("global scope(Область видимости)")
foo()

def outher_func():
    a = 20
    def inner_func():
        a = 30
        print("a =", a)
    inner_func()
    print("a =", a)
a = 10
outher_func()
print("a =", a)

a = 5
def qq():
    a= 10
    print(a)
qq()

a = 5
def qq():
    global a# Это не способствует читаемости кода.
    print(a)
    a= 10
qq()

def outer():
    x = "локальная переменная"
    def inner():
        nonlocal x
        x = "нелокальная переменная x"
        print("вложенная функция:", x)
        inner()
        print(":", x)

outer()

"""В языке программирования Python есть специальное слово — nonlocal. Оно помогает понять, что переменная, 
 которую мы используем, не является локальной для этой функции, но и не является глобальной.
 Nonlocal используется, когда мы пишем функции внутри других функций. Это помогает интерпретатору понять, 
 что переменная не принадлежит этой функции, но и не является общей для всего кода.
 Например, мы можем написать функцию, которая будет создавать другие функции."""

def get_my_func():
   def hello_world():
       print("Hello")
   return hello_world

hello_world_func = get_my_func()  # получить функцию в качестве результата

print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello

z=1
e=13
def slozhenie():
    res = z+e
    print(res)
    return(res)

slozhenie()


result = "Hello"
def test_func():
    global result
    print("переменная резалт до изменения:", result)
    result = "Hello, world!"
    print("переменная резалт после изменнеия:", result)
    return result
test_func()

def summa(c,d):
    return c+d


resultat = summa(3,4)
print(resultat)
print(summa("H","i"))


nums_1 = [5,6,8,9,0,12,13]

min = nums_1[0]
for el in nums_1:
    if el < min:
        min = el
print(min)


def ilove_you():
    Karina = "Люблю тебя"
    print(Karina)
    return Karina

ilove_you()

# Объявление функции hello()


def hello(name):
    # А здесь началось тело функции
    print('Приветствую', name)
hello("AND") 
 
# Код функции say_hello()
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')

# Дальше код написан без отступов: этот код уже вне функции.

# Несколько раз вызовем функцию say_hello() с разными аргументами:
say_hello(4)  # Вызов функции say_hello() с аргументом 4
say_hello(10)  # Вызов функции с аргументом 10
say_hello(15)  # Ещё один вызов функции
say_hello(20)  # И ещё один вызов

def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


# Ниже напишите цикл, в котором будет вызываться функция print_friends_count
# с аргументом от 0 до 20 включительно
for friends_count in range(0, 21):
    print_friends_count(friends_count)

# Количество баллов, которое студент получил за тест.
score = 60

def test_score():
    if score > 50:
        print('Отличная работа!')
        print('Тест сдан.')
    else:
        print('Хорошая попытка!')
print('Вы отлично постарались, но нужно подготовиться чуть получше.')
print('Ещё раз пройти тестирование можно в следующую среду.')

test_score()

users = ['Степан', 'Анатолий', 'Антон', 'Андрей']


def print_users(users):
    for user in users:
        print(user)

resorts = ['Сочи', 'курорты Краснодарского Края', 'Санкт-Петербург', 'Карелию']
def choose_vacation_place(resorts):
    for resort in resorts:
        if resort == 'Сочи':
            return resort
resort = choose_vacation_place(resorts)
print('Поехали в ' + resort)

def print_home(name, planet):
    print(name + ' живет на планете ' + planet)

tatooin = 'Татуин'
greeting = 'Да пребудет с тобой Сила!'
my_son = 'Люк, я твой отец!'
luke = 'Люк Скайуокер'

# Вызов функции
print_home(luke, tatooin)

# Если при вызове забудут передать имя - значением name будет слово 'Инкогнито';
# а если вызвать функцию, не передав название планеты -
# функция присвоит переменной planet значение "Икс"
def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

# Передаём только один аргумент вместо двух
print_home('Дроид-убийца')

# Значение по умолчанию будет использовано в том случае, если при вызове функции не был передан ожидаемый аргумент. 

def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)


print_home('Земля')

# Добавим значение по умолчанию для аргумента name
def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

# Передаём именованный параметр: 
# явно указываем, что значение 'Земля' предназначено для параметра planet
print_home(planet='Земля')  

# Ещё раз вызовем функцию: передадим два именованных параметра,
# но не в том порядке, как они указаны в объявлении функции:
print_home(planet='Марс', name='Марк Уотни')  

# Настройте функцию так, чтобы она не сломалась при вызове без аргументов
def lets_go(name= "Друг", target="учить Python"):
    print(name + ', пойдём ' + target)


# Вызовите функцию lets_go без аргументов
lets_go()

def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)


# Исправьте вызов так, чтобы аргумент был передан
# в параметр с именем target
lets_go(target = 'читать следующий урок!')


def int_multiple(a,b):
    res = a*b
    return int(res)

print(int_multiple(113, 2.7))
print(int(math.sqrt(int_multiple(44, 44))))

def calculate_speed(distance, time):
    print()
    return distance / time

print(calculate_speed(3.4, 20))

