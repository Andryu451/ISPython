# import numpy
# import hack4u

print("Hello, world!")
a, b = 3, 5
print(a-b)
temp = a
a = b
b = temp
print(a-b)
a = a - b
b = a + b
a = b - a
#Более формально, функция — фрагмент кода, к которому можно обратиться из любого другого места.
month = input ("Какой сейчас месяц?: ")
print("Текущий месяц -", month)
first_name = input("Введите своё имя: ")
last_name = input("Введите своё отчество: ")
age = input("Введите ваш возраст: ")
city = input("Введите гоорд проживания: ")

print("")
print("Дата: 18.10.2024")
print("")
print("Здравствуйте,", first_name, last_name,"!")
print("")
print("Ваш профиль:")
print("Возраст:", age, "лет")
print("Город проживания:", city)
a = 3.14
b = '3.14'

print(type(a))
#<class 'float'>
print(type(b))
#<class 'str'>

print ((3.14+0.3)/2+0.15)
print (3.44/2.15)

a, b = -13, 7
a = a - b
b = a + b
print(a)

s = "python"
print(s[0])
# p
print(s[1:4])
# yth

#Несмотря на то, что мы можем прочитать отдельный символ, перезаписать мы его не можем,
#потому что строки являются неизменяемыми данными:
# s = "python"
# s[0] = 'C'
# print(s)
# ожидается вывод "Cython", однако Python вернёт ошибку:
# TypeError: 'str' object does not support item assignment
# Логические значения можно получать и как возвращаемое значение некоторых действий, таких как сравнение:
print(3 > 10)
# False
print(3 < 10)
# True
print(3 == 10) # равны ли объекты?
# False
# Можно также проверить, содержится ли какой-то символ в строке:
print('r' in 'world') # проверяем отдельный символ
# True
print('th' in 'python') # проверяем целую подстроку
# True
print('the' in 'python')
# False

k = 1.57*3/1.5==3.14
print(k)

# Для сохранения нескольких объектов (необязательно текстовых) в одну переменную можно использовать кортежи (tuple).
# Чтобы создать кортеж, нужно записать данные в круглые скобки через запятую:
date = (22, 'October', 2024)
print(date)

s1 = "foo"
s2 = "bar"
s1 = s1+s2
print(s1)
# foobar

a = 5
b = 2
q = a // b # q = 2
r = a % b  # r = 1

a_2= 5
b = 2
q = a // b # q = 2
r = a % b  # r = 1
print ((31%2) + (-31 % 2))

print (13%-3*3-3**2)
a= 5.4321
print(a**100)
# 3.138886636534116e+73
#[мантисса]e[показатель <>степени <>числа 10]

print(round(11*2.5/3, 2))

pi = 3.14159
print(round(pi**2/2))

s = "Hello!"

print(s[0])
# H

print(s[4])
# o

s = "Hello!"
print(s[::2])
#Отрицательный шаг позволяет развернуть строку:

print(s[::-1])
# !olleH

# Отрицательным может быть не только шаг, но и сам индекс. Отрицательные индексы нумеруются от последнего символа к первому:

print(s[-1])
# !

print(s[-3:-1])
# lo

# Встроенная функция len() позволяет узнать длину строки:
print(len(s))
# 6

# Метод find(substr), определённый для строк, позволяет находить символы и подстроки:

print(s.find('e')) # возвращает индекс
# 1

print(s.find('o!')) # в случае подстроки возвращает индекс первого символа
# 4

#Метод find(substr), определённый для строк, позволяет находить символы и подстроки:

print(s.find('e')) # возвращает индекс
# 1

print(s.find('o!')) # в случае подстроки возвращает индекс первого символа
# 4

#Приведённые ниже методы позволяют привести все буквы к верхнему регистру (заглавным буквам) или к нижнему регистру (строчным буквам). Обратите внимание, что исходная строка не изменяется:

print(s.upper())
# HELLO!

print(s.lower())
# hello!

print(s)
# Hello!

print(s.isdigit()) # строка состоит из цифр?
# False

print(s.isalpha()) # строка состоит из букв?
# False
print(s.isalnum()) # строка состоит из цифр и букв?
# False

colors = 'red blue green'
print(colors.split())
colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue

#Задание 3.8.1
# Ввод чисел через пробел
numbers = input("Введите числа через пробел: ")

# Разделение строки на отдельные числа и объединение с переносами строк
print('\n'.join(numbers.split()))

age = 25

my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d

print(my_age)
# I'm 25 years old
#Мы создали строковую переменную, в середину которой поместили число без необходимости разбивать строки на несколько
#и потом склеивать их. Чтобы это сделать, в шаблоне строки необходимо указывать место и тип объекта, который нужно 
#поместить на это место, помещая специальный символ %d. Он указывает, что на этом месте должно стоять целое число (digit).

pi = 3.14159265
print ("%.4e" % (pi))

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14

#Как должен выглядеть шаблон строки для вывода времени в записанном ниже формате?
#HH:MM:SS
#Вставьте нужный шаблон вместо знаков "???", используя только специальный символ «%d».
#print("???"% (hours, minutes, seconds))
#%02d:%02d:%02d

# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']

# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('e')

print(letters)
# ['a', 'b', 'c', 'd', 'e']

#Как и ожидалось, длина списка равна 5. Тогда доступ к последнему элементу можно получить, если уменьшить эту длину на 1:

print(letters[len(letters)-1])
# e

#Если мы добавим ещё какое-то количество элементов в список, такой способ будет продолжать работать:

letters.append('f') # добавляем ещё одну букву
letters.append('g') # и ещё одну

print(letters[len(letters)-1])
# g

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters.pop() # вызов метода без аргументов удаляет последний элемент списка

#Python не ограничивает мощь своего функционала доступом к элементам по индексам и отрицательным индексам.
#С помощью срезов можно получать сразу несколько элементов списка.
#[:]-Возвращает элементы полностью	[‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
# [2:]-Возвращает элементы списка, начиная с элемента индекса 2 и до конца списка	[‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
# [:3]-Возвращает элементы списка от его начала до элемента с индексом 3, не включая его	[‘a’, ‘b’, ‘c’]
# [1:4]-Объединяя предыдущие два способа можно получить элементы из середины.
# [::2]-Задаёт шаг, через который извлекаются элементы	[‘a’, ‘c’, ‘e’, ‘g’]
# [::-1]-Используя отрицательный шаг, можно развернуть массив	[‘g’, ‘f’, ‘e’, ‘d’, ‘c’, ‘b’, ‘a’]

qwerty=[1.0,2.1,3.3,4.6,5.7,6.8]
print(map(round, qwerty))
print(list(map(round,qwerty)))

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[ 3::-1 ])
# [1, "в", "б", "а"]

L = ["а", "б", "в", 1, 2, 3, 4]
print(L[ 6:3:-1])
# [4, 3, 2]

# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6] 

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]

# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6] 

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]

person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

person.pop('phone')

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}

# Что выведет программа? Впишите получившуюся строку без использования кавычек.

d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))

abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}

abits = [abit1, abit2, abit3]

print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True},
# {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False},
# {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}]

abit4 = {"ФИО" : 'Любимчиков А.Я.', "Количество баллов" : 269, "Заявление" : True}

abits.append(abit4)

print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True},
# {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False}, 
# {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True},
# {'ФИО': 'Любимчиков А.Я.', 'Количество баллов': 269, 'Заявление': True}]

L = [1,1,2,3,2]

b = set(L)

print(b)
# {1,2,3}

b_list = list(b)

print(b_list)
# [1,2,3]

text = "The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"

unique = list(set(text))

print("Количество уникальных символов: ", len(unique))

abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors = abons.difference(debtors)

print(non_debtors)
# {'Васильев', 'Иванов'}

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.union(b_set)

print(a_and_b)

# Напишите числа в порядке возрастания через пробел, которые выведет программа из предыдущего задания,
# если на вход подаются две последовательности чисел:

# 1 2 3 4 5 6 7 8
# 2 4 6 8 10 12
