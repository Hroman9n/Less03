b="Buzz"
f="Fizz"

for i in range(101):    # берем 101, потому что range(n) создает массив от 0 до n-1
    if i % 15 == 0:
        print(f+b)
    elif i % 5 == 0:
        print(b)
    elif i % 3 == 0:
        print(f)
    else:
        print(i)
