
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

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[ 3::-1 ])
# [1, "в", "б", "а"]

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[ 6:3:-1 ])
# [4, 3, 2]


# Возможности языка позволяют выполнить определённые действия для каждого элемента списка.
# Такую операцию можно проделать с помощью функцию map():

# map(function, list)
# Первый аргумент map() — функция, которую нужно применить к каждому элементу списка, а сам список — второй аргумент. 
# Возвращаемое значение этой функции — объект map, который можно преобразовать, например, обратно в список.

# Рассмотрим пример:

# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6] 

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

# Как и в случае списков, словарь можно создать пустым, можно сразу наполнить его объектами, а можно расширять постепенно:

person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

# Из словаря аналогично спискам можно удалить объект по его ключу. 
# Важно помнить, что словарь является неупорядоченным, поэтому в функцию pop() всегда нужно передавать ключ удаляемого объекта:

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

person.pop('phone')

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}

# Что выведет программа? Впишите получившуюся строку без использования кавычек.

d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))

title = input("Введите название книги:")
author = input("Введите фамилию автора:")
year = int(input("Введите год издания:"))

book = {'title' : title,
        'author' : author,
        'year' : year}
           
print(book)

abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}


abits = [abit1, abit2, abit3]

print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True},
#  {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False},
#  {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}]

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

c = list(set(L))

print(c)
# [1,2,3]

text = "The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
unique = list(set(text))

print("Количество уникальных символов: ", len(unique))

# Множества в Python аналогичны математическим множествам, поэтому для них существует несколько собственных операций.
# Операция	Название	Смысл
# set.union(other)|	Объединение | Возвращает множество, состоящее из элементов set и other.
# set.intersection(other) | Пересечение | Возвращает множество, состоящее из элементов, которые встречаются и в set, и в other.
# set.difference(other) | Разность | Возвращает множество элементов set, которые не встречаются в other.
# set.symmetric_difference(other) | Симметричная разность | Возвращает множество, включающее все элементы исходных множеств,
# которые не принадлежат обоим одновременно.


abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors = abons.difference(debtors)

print(non_debtors)
# {'Васильев', 'Иванов'}

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)


