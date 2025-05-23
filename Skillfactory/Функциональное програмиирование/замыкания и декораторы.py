
import webbrowser
import time
'''Функции высшего порядка
 Функция высшего порядка — в программировании это функция, принимающая в качестве аргументов другие функции
 или возвращающая другую функцию в качестве результата.

 Основная идея состоит в том, что функции имеют тот же статус, что и другие объекты данных.

 Мы можем передавать функции как параметры:
 def my_func(inside_func):
     inside_func()  # Вызов функции принятой в качестве аргумента

 def a():
     def b(): 
         pass
     return b'''

"""Для лучшего понимания функций высшего порядка можно представить себе конвейер, который собирает других роботов. 
То есть некая техника собирает другую технику.

Сделаем функцию, которая будет выполнять принимаемую функцию дважды:"""

def twice_func(inside_func):
   """Функция, выполняющая дважды функцию, принятую в качестве аргумента"""
   inside_func()
   inside_func()

def hello():
   print("Hello")
  
test = twice_func(hello)
# Hello
# Hello
# Видим, что после передачи функции hello в качестве аргумента для функции twice_func, она выполнялась в ней дважды. 
# Теперь перейдём к теме замыкания функций и разберём, что это такое.

# Замыкание в программировании — это функция, в теле которой присутствуют ссылки на переменные, объявленные вне тела этой функции в окружающем коде и не являющиеся её аргументами.
# Вспомните нелокальную (nonlocal) область видимости, на этом принципе работает замыкание функций.

# Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и тоже число x:

def make_adder(x):
   def adder(n):
       return x + n # захват переменной "x" из nonlocal области
   return adder  # возвращение функции в качестве результата
# То есть мы сделали конвейер, который будет нам прибавлять фиксированное число x к любому числу n (см. функции высших порядков). Тогда сделаем функцию, которая будет прибавлять число 5 к любому числу.

# функция, которая будет к любому числу прибавлять пятёрку
add_5 = make_adder(5)
print(add_5(10))  # 15
print(add_5(100))  # 105
# Определив функции высших порядков и замыкание функций, давайте перейдём к теме декораторов, которая основывается на них.

# Декораторы предназначены для подключения любого дополнительного поведения к основной функции, называемой декорируемой функцией,
#  которое может выполняться до, после или даже вместо основной функции. При этом исходный код декорируемой функции никак не затрагивается.

# В качестве дополнительного поведения может выступать подсчёт времени выполнения функции,
#  проверка дополнительных условий, разрешающих выполнение указанной функции.
def my_decarator(a_function_to_decorate):
   def wrapper():
      result = a_function_to_decorate()
      return result
   return wrapper
# На рисунке выше представлен простейший декоратор, который не выполняет никаких дополнительных действий.

# Желтым выделена декорируемая функция, которая принимается декоратором my_decorator в качестве аргумента благодаря функциям высшего порядка. 
# Далее декорируемая функция через замыкание передаётся в декорированную функцию wrapper.
# И уже декорированную функцию, которая как раз и может добавлять дополнительное поведение к основной, возвращает сам декоратор (57-61).

# Давайте посмотрим на примере, как добавить дополнительное поведение к основной функции.

def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обёртку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, который будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")
        
        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
        
        print("Я буду выполнен после основного вызова!")
        return result
    return wrapper
# Наш декоратор будет печатать строку «Я буду выполнен до основного вызова!» перед основным вызовом, 
# а строка «Я буду выполнен после основного вызова!» соответственно после основного вызова. Если необходимо, 
# то не забываем вернуть результат исходной функции.
def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0


# def validator(func):
#    def wrapper(url):
#       if "." in url:
#          func(url)
#       else:
#          print("Неверный URL")
         
#    return wrapper

# @validator
# def open_url(url):
#    webbrowser.open(url)

# open_url("https://vk.com/kari_lav")


# определение функции декоратора
def select(input_func):
    def output_func():
        print("*****************")  # перед выводом оригинальной функции выводим звёздочки
        input_func()  # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим звёздочки
    return output_func  # возвращаем новую функцию

# определение оригинальной функции
@select  # применение декоратора select
def hello():
    print("Hello METANIT.COM")

# вызов оригинальной функции
hello()

def my_decor(func):
    def wrapper():
        print(f'start')
        func()
        print(f'end')
    return wrapper

@my_decor

def my_func():
    print(f'тут основная функция')

my_func()
hello()

def my_decorator(a_function_to_decorate):
    x = "*********@@@@@$$$$$*********"
    print(str(x))
    # Здесь мы определяем новую функцию - «обёртку». Она нам нужна, чтобы выполнять каждый раз при вызове оригинальной функции, а не только один раз.
    def wrapper():
        # здесь поместим код, который будет выполняться до вызова, потом вызов оригинальной функции, потом код после вызова.
        print("Я буду выполнен до основного вызова!")
        
        result = a_function_to_decorate()  
        
        print("Я буду выполнен после основного вызова!")# не забываем вернуть значение исходной функции
        return result
    return wrapper

def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0
# Видим, что задекорировав my_function, мы добавили к ней новый функционал, не меняя исходный код самой функции.

# Зачем это нужно? Например, декораторы могут замерять время выполнения функции либо количество запусков конкретной функции, 
# также можно сохранять результаты вычисления (кеширование).
# Давайте попробуем замерить время выполнения системной функции для возведения числа в степень 2 и соответствующего оператора.


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458

# Задание 5.5.1
# Задание на самопроверку.

# Взять из предыдущего примера декорированные функции, которые возвращают время работы основной функции, 
# и найти среднее время выполнения для 100 выполнений каждой функции.

# Решение


N = 100


def decorator_time(fn):
   def wrapper():
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       return dt
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
   mean_pow_2 += pow_2()
   mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")

# Синтаксический сахар в языке программирования — это синтаксические возможности, применение которых не влияет на поведение программы, 
# но делает использование языка более удобным для человека.
# Пользоваться им можно так:

@my_decorator
def my_function():
    pass
# При этом будет происходить всё то же самое, аналогичное.

my_function = my_decorator(my_function)
# Имейте в виду, что при использовании синтаксического сахара на месте декорируемой функции появляется задекориванная функция!

def my_decorator(fn):
   def wrapper():
       fn()
   return wrapper  # возвращается задекорированная функция, которая заменяет исходную

# выведем незадекорированную функцию
def my_function():
   pass
print(my_function)  # <function my_function at 0x7f938401ba60>

# выведем задекорированную функцию
@my_decorator
def my_function():
   pass
print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>

# Видим, что после декорирования под названием исходной функции будет не сама функция, а функция, которая была внутри декоратора, 
# в данном случае функция wrapper.

# Передача аргументов в декорируемую функцию
# До этого мы с вами декорировали только функции без аргументов. Но что будет, если мы попытаемся задекорировать функцию с аргументами?

# def do_it_twice(func):
#     def wrapper():
#         func(arg)
#         func(arg)
#     return wrapper

# @do_it_twice
# def say_word(word):
#     print(word)

# say_word("Oo!!!")
# При выполнении данного кода будет выведена такая ошибка:

# TypeError: wrapper() takes 0 positional arguments but 1 was given

# декоратор, в котором встроенная функция умеет принимать аргументы
def do_it_twice(func):
   def wrapper(*args, **kwargs):
       func(*args, **kwargs)
       func(*args, **kwargs)
   return wrapper

@do_it_twice
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Oo!!!

# Подведём итог по декораторам:

# Декораторы добавляют дополнительное поведение функции без изменения её исходного кода.
# Декораторы —  вызовы дополнительных функций, поэтому они немного замедляют ваш код.
# Для передачи аргументов декорируемой функции используйте *args и **kwargs.
# Вот универсальный шаблон для декоратора:

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper


# Задание 5.5.2
# Задание на самопроверку.

# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.

# Решение
def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)
       count += 1
       print(f"Функция {func} была вызвана {count} раз")
   return wrapper

@counter
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз
# Задание 5.5.3
# Задание на самопроверку.

# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре. Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент функции, по значению — результат работы функции, например, {n: f(n)}.

# И при повторном вызове функция будет брать значение из словаря, а не вычислять заново. То есть словарь можно считать промежуточной памятью на время работы программы, где будут храниться ранее вычисленные значения. Исходная функция, которую нужно задекорировать, имеет следующий вид и выполняет простое умножение на число 123456789.:

def f(n):
   return n * 123456789

# Решение
def cache(func):
   cache_dict = {}
   def wrapper(num):
       nonlocal cache_dict
       if num not in cache_dict:
           cache_dict[num] = func(num)
           print(f"Добавление результата в кеш: {cache_dict[num]}")
       else:
           print(f"Возвращение результата из кеша: {cache_dict[num]}")
       print(f"кеш {cache_dict}")
       return cache_dict[num]
   return wrapper
