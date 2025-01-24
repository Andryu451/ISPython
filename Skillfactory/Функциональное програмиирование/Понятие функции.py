# Функция – это блок кода, который начинается с ключевого слова def, затем следует название функции, затем скобки, в которых указываются аргументы 
# функции, и двоеточие в конце. Со следующей строки начинается тело функции.
# Это именно тот участок, который будет выполняться при вызове функции.

def name_func():
    # начало тела функции
    ...
    # конец тела функции

# В нашем случае мы можем сделать отдельную функцию подсчёта частоты символов текста. Назвать её соответствующим образом — char_frequency, а дальше внутри программы обращаться к нашей функции и по названию сразу понять, что происходит в данной части программы.

# объявили функцию для подсчёта количества символов в тексте
def char_frequency():
   text = """
   У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   Идёт направо -- песнь заводит,
   Налево -- сказку говорит.
   Там чудеса: там леший бродит,
   Русалка на ветвях сидит;
   Там на неведомых дорожках
   Следы невиданных зверей;
   Избушка там на курьих ножках
   Стоит без окон, без дверей;
   Там лес и дол видений полны;
   Там о заре прихлынут волны
   На брег песчаный и пустой,
   И тридцать витязей прекрасных
   Чредой из вод выходят ясных,
   И с ними дядька их морской;
   Там королевич мимоходом
   Пленяет грозного царя;
   Там в облаках перед народом
   Через леса, через моря
   Колдун несёт богатыря;
   В темнице там царевна тужит,
   А бурый волк ей верно служит;
   Там ступа с Бабою Ягой
   Идёт, бредёт сама собой,
   Там царь Кащей над златом чахнет;
   Там русский дух... там Русью пахнет!
   И там я был, и мёд я пил;
   У моря видел дуб зелёный;
   Под ним сидел, и кот учёный
   Свои мне сказки говорил.
   """

   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчёта символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")


# вызвали функцию в любом месте программы
char_frequency()

def print_2_add_2():
   result = 2 + 2
   print(result)

print_2_add_2()

def hello_world():
    Hello_world = "Hello, world!"
    print(Hello_world)

hello_world()

# объявили функцию для подсчёта количества символов в неком абстрактном тексте
def char_frequency(text):
   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчёта символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")

def prinhelworld():
     result = "Hello, world!"
     print(result)

prinhelworld()

def pr2_add_2():
    print(2+2)

pr2_add_2()

def pow_func(base):
    print(base**2)
pow_func(4)
pow_func(13)

def pow_func2(bas, n=2):
    print(bas**n)
pow_func2(4)
pow_func2(2, 6)

def check_num(a, n):
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5

def reverse_stair(n):
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(5)

def pow_func(base, n=2):
   print(base ** n)

print(pow_func(3)) 
# 9
# None

# Видим, что помимо результата вычисления вывелось ещё значение None. Дело в том, что функции в Python всегда что-то возвращают, 
# и если вы этого не указали, то автоматически интерпретатор подставит за вас строку return None в конец вашей функции. 
# То есть её код в явном виде будет выглядеть следующим образом:

def pow_func(base, n=2):
   print(base ** n)
   return None

print(pow_func(3)) 
# 9
# None


def chek_sum(a,b):
    if a%b == 0:
        print(f"Число {b} является делителем числа {a}")
    else:
        print(f"Число {b} не является делителем числа {a}")
    return None
chek_sum(2, 5)

def get_multipliers(a):
   count = 1
   for n in range(1, a // 2 + 1):
       if a % n == 0:
           count += 1

   return count

get_multipliers(5)  # 2
get_multipliers(4)  # 3

def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True

# Вебинар:
def my_func():
    a = 4
    b = 9
    print(a+b)

my_func()

def my_funk(a,b):
    print(a+b)

my_funk(10,12)

def my_funck(a, b):
    result= a + b
    return(result)

c = my_funck(13, 12)
print(c)