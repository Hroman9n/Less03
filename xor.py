from itertools import cycle

def do_cipher(string, key):
    return ''.join(chr(ord(s) ^ ord(k)) for (s, k) in zip(string, cycle(key)))


key = "01000"
String = "11101"

# key = input("Key: ")
# String = input("Phrase: ")
result = do_cipher(String, key)

# print(str.encode(result))
print(result)
print(do_cipher(result, key))