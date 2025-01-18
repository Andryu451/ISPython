print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 21, 2)))
S = 0
N = 5
for i in range(1, N+1):
    print("Значение суммы на предыдущем шаге:", S)
    print("Текущее число:", i)
    S = S+i
    print("Значение суммы после сложения:", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна =", S)

P = 1
N = 5
for k in range(1, N+1):
    P*=k
print(P)

N = 5

for i in range(1, N + 1):
   print("*" * i)

S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать, пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счётчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n)

n = 1
while True:
   if n ** 2 >= 1000:
       print("Последнее число", n - 1)
       break
   n += 1

# плохо
n = 1
# while n < 10:  # в данной программе это условие всегда True, цикл будет бесконечным
    # print("Hello World")

# хорошо
n = 1
while True:  # в данной программе это условие всегда True, цикл будет бесконечным
   print("Hello World")
   n += 1
   if n > 10:  # условие, при достижении которого цикл while будет принудительно завершён
       break

N = 2
M = 3
# заполнили матрицу последовательными числами
matrix = [
    [0, 1, 2], 
    [3, 4, 5], 
]


for i in range(N):  # цикл, отвечающий за строки
    for j in range(M):  # цикл, отвечающий за столбцы
        print(matrix[i][j], end=" ")
# 0 1 2 3 4 5

for i in range(N): 
    for j in range(M): 
        print(matrix[i][j], end=" ")
    print()  # перенос на новую строку

# 0 1 2
# 3 4 5

random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берём каждую сроку
   min_index = 0  # в качестве минимального значения возьмём первый элемент строки
   max_index = 0
   min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
   max_value = row[max_index]  # для максимального значения то же самое
   for index_col in range(len(row)):
       if row[index_col] < min_value:
           min_value = row[index_col]
           min_index = index_col
       if row[index_col] > max_value:
           max_value = row[index_col]
           max_index = index_col
   min_value_rows.append(min_value)
   min_index_rows.append(min_index)
   max_value_rows.append(max_value)
   max_index_rows.append(max_index)
  
print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)


