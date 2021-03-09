from itertools import cycle     # необходимо для прокручивания ключа

def do_cipher(string, key):
    return ''.join(chr(ord(s) ^ ord(k)) for (s, k) in zip(string, cycle(key)))
        #  ^                                здесь мы идем по строке, и ключу
        # пустая строка,                    прокручивая бесконечно ключ (cycle)
        # к которой доба-                   объединяя числ. представление  
        # вляются символы                   каждого символа и получаем новый

### тестовые значения ###
# key = "01000"
# key = "fox"
# key = "midnight"
# String = "11101"
# String = "hello, my name is Sergei, nice to meet you"
# String = "It WaS a GrEaT dAy"


key = input("Key: ")
String = input("Phrase: ")

result = do_cipher(String, key)

print(str.encode(result))
print(do_cipher(result, key))