for i in range(101):    # берем 101, потому что range(n) создает массив от 0 до n-1
    str = ""
    if i % 3 == 0:
        str = "Fizz"
    if i % 5 == 0:
        str += "Buzz"
    if str == "":
        str = i
    print(str)
