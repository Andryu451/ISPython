# Синтаксис функций-генераторов отличается от обычных функции только оператором yield, он используется вместо оператора return.
# В обычной функции, когда интерпретатор встречает в теле функции оператор return, то он выходит из тела функции и возвращается к основной программе.
# Встречая же yield, он понимает, что функцию-генератор закрывать не нужно, а нужно приостановить и затем вернуться к ней.
# def fib():
#    a,b = 0,1
#    yield a
#    yield b

#    while True:
#       a, b = b, a + b
#       yield b
# for num in fib():
#    print(num)

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value

# for i in repeat_list([1, 2, 3]):
#    print(i)

# Итератор (iterator) — это объект, который возвращает свои элементы по одному за раз.
# В качестве итератора могут выступать следующие объекты: функции-генераторы, которые мы прошли, 
# а также последовательности после проведения над ними некоторых операций. Если вы не знаете, является ли объект итерируемым, 
# можно использовать функцию iter(object) и передать ей в качестве аргумента объект для проверки. Если объект итерируемый, 
# то вам вернется итератор, если нет, то будет соответствующая ошибка.


# Логика работы с итераторами в языке Python следующая:
#     Получаем итератор с помощью функции iter(iterable_object).
#     Вызываем много раз next(iterator) от полученного итератора.
#     Когда получим ошибку StopIteration — прекращаем работу.

# В качестве примера возьмём строку и получим от неё итератор:

# для примера возьмём строку
str_ = "my tst"
str_iter = iter(str_)

print(type(str_))  # строка
print(type(str_iter))  # итератор строки

# Получим первый элемент строки
print(next(str_iter))  # m
# Получим ещё несколько элементов последовательности
print(next(str_iter))  # y
print(next(str_iter))  #
print(next(str_iter))  # t
print(next(str_iter))  # s
print(next(str_iter))  # t


def count(start, step):
     counter = start
     while True:
         yield counter
         counter += step

my_gen_func = count(100, 10)
for i in range(21):
     print(next(my_gen_func))

id (my_gen_func) == id (iter(my_gen_func))


def first_gen(input_):
     yield input_
     input_+= 1
     print(input_)

my_first_gen = first_gen(5)
print(next(my_first_gen))

def fib():
     a, b = 0,1
     yield a
     yield b 

     while True:
          a, b = b, a+b
          yield b
     
for i in fib():
     print(i)