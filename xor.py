from itertools import cycle     # необходимо для прокручивания ключа

def do_cipher(string, key):
    return ''.join(chr(ord(s) ^ ord(k)) for (s, k) in zip(string, cycle(key)))
        #  ^                                здесь мы идем по строке, и ключу
        # пустая строка,                    прокручивая бесконечно ключ (cycle)
        # к которой доба-                   объединяя числ. представление  
        # вляются символы                   каждого символа и получаем новый

# если на вход подаётся двоичная строка
def do_cipher_bin(bi, key):
    res = ""

    for (b, k) in zip(bi, cycle(key)):
        l = int(b)
        r = int(k)
        res += str((l + r) % 2)
    return res


### тестовые значения ###
# key = "fox"
# key = "101"
# key = "midnight"
# String = "hello, my name is Sergei, nice to meet you"
# String = "It WaS a GrEaT dAy"
# String = "110110101"


key = input("Key: ")
String = input("Phrase: ")

print(f'Исходное сообщение: {String}')

try:
    # проверяем введено ли двоичное число
    binaryS = bin(int(String, 2))
    binaryK = bin(int(key, 2))
    result = do_cipher_bin(String, key)
    print(f'Зашифрованное сообщение (двоичная строка): {result}')
    flag = "b"
except ValueError:
     # если не двоичное то шифруем как обычно
    result = do_cipher(String, key)
    print(f'Зашифрованное сообщение: {str.encode(result)}')
    flag = "n"


ask = input("Хотите дешифровать сообщение по тому же ключу (да или нет)?: ")

if ask == "да":
    # обратное шифрование
    if flag == "n":
        print(f'Дешифровка: {do_cipher(result, key)}')
    elif flag == "b":
        print(f'Дешифровка: {do_cipher_bin(result, key)}')
elif ask == "нет":
    print("Заканчиваю работу")
    exit()
else:
    print(f"Введено ни да, не нет, посчитаем это за нет (было введено: {ask})")
    exit()