print(list(str(123456789)))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_digit = list(map(int, list(str(123456789))))
print(5 in list_digit)
# True

print('5' in str(123456789))
# True

# Дано n-значное целое число N. Определить: входят ли в него цифры 3 и 7.

'3' in str(N) and '7' in str(N)

a = [1, 2, 3]
print(id(a))  # id возвращает идентификатор объекта
# 140039772293512

b = a
print(id(b))
# 140039772293512

print(a is b)  # а и b являются один и тем же объектом
# True
