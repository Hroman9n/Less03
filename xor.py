from itertools import cycle     # необходимо для прокручивания ключа

def do_cipher(string, key):
    return ''.join(chr(ord(s) ^ ord(k)) for (s, k) in zip(string, cycle(key)))
        #  ^                                здесь мы идем по строке, и ключу
        # пустая строка,                    прокручивая бесконечно ключ (cycle)
        # к которой доба-                   объединяя числ. представление  
        # вляются символы                   каждого символа и получаем новый

### тестовые значения ###
# key = "fox"
# key = "midnight"
# String = "hello, my name is Sergei, nice to meet you"
# String = "It WaS a GrEaT dAy"


key = input("Key: ")
String = input("Phrase: ")

result = do_cipher(String, key)

print(f'Исходное сообщение: {String}')
print(f'Зашифрованное сообщение: {str.encode(result)}')

ask = input("Хотите дешифровать сообщение по тому же ключу (да или нет)?: ")

if ask == "да":
    # обратное шифрование
    print(do_cipher(result, key))
elif ask == "нет":
    print("Заканчиваю работу")
    exit()
else:
    print(f"Введено ни да, не нет, посчитаем это за нет (было введено: {ask})")
    exit()