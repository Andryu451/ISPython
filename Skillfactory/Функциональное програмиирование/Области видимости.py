# # В Python существует 3 области видимости:

# локальная,
# глобальная,
# нелокальная (добавлена в Python 3)

def local():
   x = 5  # локальная переменная
   print(x)

x = 10
local()
print(x)

# 5
# 10
def local():
   print(x)  # так как x нет в локальной области видимости, мы берём её из глобальной области

x = 105
local()
print(x)

# 10
# 10
# Если запустить данный код, то мы увидим, что распечаталось два раза значение 105. Это происходит, потому что, не найдя переменной в локальной области,
# функция обращается к глобальной области видимости, которая находится на уровне модуля, и берёт значение оттуда.
# И здесь не нарушается так называемое «правило бункера». Из бункера мы можем увидеть, что происходит во внешнем мире, но вот наоборот это не работает.

x = 33
def function():
    print(x)
    return x

print(function())

x = 45
def func():
   print(x)
   x = 5
   x += 5
   return x

# print(func())

# Ошибка возникает, потому что Python замечает, что вы пытаетесь распечатать значение локальной (!) переменной х в функции func до её объявления,
# что и приводит к ошибке, так как х ещё не определён.(область видимости переменной (где она может использоваться) всегда определяется местом, где ей было присвоено значение.)

# Как обойти это ограничение? Нужно использовать оператор global, который объявляет переменную доступной для блока кода, следующим за оператором. 
# Давайте попробуем использовать глобальную область видимости для исправления нашей ошибки из предыдущего примера:

x = 1020201

def funcshn():
   global x # объявляем, что переменная является глобальной
   print(x)
   x = 5
   x += 6
   return x

funcshn()
print(x)

#Функции образуют локальную область видимости, а скрипты (программы) — глобальную.
#Эти две области взаимосвязаны между собой следующим образом: каждый скрипт — это глобальная область видимости, 
#то есть пространство имён, в котором создаются переменные на уровне файла.


# Нелокальная область видимости
# Появилось это понятие в Python 3 вместе с ключевым словом nonlocal. Логика его написания примерно такая же, как и у global. 
# Но у nonlocal есть особенность. Nonlocal используется чаще всего во вложенных функциях, когда мы хотим дать интерпретатору понять, 
# что для вложенной функции определённая переменная не является локальной, но она и не является глобальной в общем смысле. 
# Предположим, мы хотим сделать функцию, которая будет возвращать нам функции (да, в Python такое возможно).

# Рассмотрим такой пример:

def get_my_func():
   def hello_world():
       print("Hello")
   return hello_world

hello_world_func = get_my_func()  # получить функцию в качестве результата

print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello

def get_mul_func(m):
   nonlocal_m = m
   def local_mul(n):
       return n * nonlocal_m
  
   return local_mul

two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
two_mul(5)  # 5 * 2

def my_func(a,b):
   result = a+b
   return result

c = my_func(5, 10)
print(c)

def my_print():
   print(c)

my_print()


#плохой стиль написания кода
PI = 3.14#глобальная переменная
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
#НЕ ИЗМЕНЯТЬ ЗНАЧЕНИЕ ФУНКЦИИ ВНУТРИ ФУНКЦИИ

# Запакованные переменные, или что такое *args и **kwargs
# Для начала давайте разберёмся с позиционными (positional) и именованными (keyword) аргументами. 
# Из названий можно предположить, что одни аргументы зависят от позиции, а вторые — от имени, всё логично.
def func(a, b, c):
   print('a =', a)
   print('b =', b)
   print('c =', c)

func(1, 2, 3)
# a = 1
# b = 2
# c = 3

func(3, 2, 1)
# a = 3
# b = 2
# c = 1

# Но никто не запрещает нам обращаться к переменным прямо по имени:

func(a=1, b=2, c=3)
# a = 1
# b = 2
# c = 3

func(c=3, b=2, a=1)
# a = 1
# b = 2
# c = 3
# Важная особенность: все именованн
# func(a, b, c=3)

# Неправильно
# func(a=1, b, c)
a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
# [[1, 2, 3], 4, 5, 6]

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
# [1, 2, 3, 4, 5, 6]

# Чтобы правильно обрабатывать *args и **kwargs нужно представлять, чем они являются. А собственно args — это кортеж, а kwargs  — это словарь.

def my_func(*args, **kwargs):
   print(type(args))
   print(type(kwargs))

my_func()
# <class 'tuple'>
# <class 'dict'>


def adder(*nums):
   sum_ = 0
   for n in nums:
       sum_ += n
  
   return sum_

print(adder())  # 0
print(adder(1))  # 1
print(adder(1, 2))  # 3
print(adder(1, 2, 3))  # 6

# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
def mul(*nums):
   p = 1
   for n in nums:
       p *= n
  
   return p


# Аргументы по умолчанию создаются один раз в момент инициализации функции (первого прочтения интерпретатором инструкции def), 
# а не при каждом вызове функции. Если в качестве аргументов по умолчанию использовать изменяемые типы данных (списки, словари),
# то они создаются один раз и будут использоваться на протяжении времени жизни функции. Так как при передаче словаря передаются не все его значения,
# а указатель на первый его элемент.

# Создадим неправильную функцию incorrect_func с указанием аргумента по умолчанию в виде списка. И вызовем эту функцию два раза.

def incorrect_func(name_arg=[]):
   # name_arg является локальной переменной
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
incorrect_func()
print('-----')
incorrect_func()

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [1]
# Аргумент после изменения [1, 1]

# Видим, что при одних и тех же входных данных функция выдаёт разные результаты, что в дальнейшей разработке может вводить в заблуждение. 
# Если вдруг внутри функции нужно использовать списки, то этот момент можно обойти следующим образом:

# установим аргумент name_arg пустым, а внутри функции будем проверять его
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
print("correct func")
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[123])

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]

def i_love_you():
   Karina = "Люблю тебя, Кариша"
   print(Karina)
   return(Karina)

i_love_you()


# Рекурсивные функции
# Рекурсивная функция — это функция, вызывающая сама себя и обрабатывающая полученный результат до тех пор, 
# пока не достигнем терминального условия (условия остановки).
# Количество раз, сколько функция вызвала сама себя, называется глубиной рекурсии.

