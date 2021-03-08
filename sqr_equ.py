from math import sqrt


def line_input():   # ввод коэффициентов в одну строку
    coef = list(input("please, enter coefficients in line with spaces between: ").split()) #

    abc = list(map(int, coef))

    return(abc)

def sep_input():    # ввод коэффициентов по отдельности
    print("please, enter coefficients separately")

    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))

    abc = [a, b, c]

    return(abc)

def a0(abc):    # если а=0 (3х+15=0)
    b = abc[1]
    c = abc[2]

    res = -c/b

    print(f"\nкорень уравнения x ={res}\n")

def b0(abc):    # если b=0 (x^2-16=0)
    a = abc[0]
    c = abc[2]

    # Если с положительное, то корней не будет
    if c < 0:
        res = sqrt(-(c/a))
        print(f"\nКорни квадратного уравнения: х1 = {-res}, x2 = {res}\n")
    else:
        res = (-(c/a))**0.5
        print(f"\nКорни квадратного уравнения (комплексные числа): х1 = {-res}, x2 = {res}\n")


def c0(abc):    # если с=0 (2х^2+8х=0)
    a = abc[0]
    b = abc[1]

    res = -b/a

    print(f"\nКорни уравнения: х1 = 0, х2 = {res}\n")

def roots(abc): # Стандартная функция вычисления квадратного уравнения
    a = abc[0]
    b = abc[1]
    c = abc[2]

    d = b**2 - 4*a*c
    dsqr = d**0.5

    x1 = (-b + dsqr)/(2*a)
    x2 = (-b - dsqr)/(2*a)

    if d < 0:       # x^2-6x+13 res: 3+2j и 3-2j
        print(f"\nКорни квадратного уравнения(комплексные числа): х1 = {x1}, x2 = {x2}\n")
    if d > 0:
        print(f"\nКорни квадратного уравнения: х1 = {x1}, x2 = {x2}\n")

    

### Конец объявления функций, основное тело программы 


abc= list() # пустой список, в который позже запишутся коэффициенты

while 1:

    mthd = input("""are you gonna write coefficients in line (enter line) or separately (enter sep)
if you want to exit from program write exit: """)

    if mthd == "exit":
        exit()
    elif mthd == "line":
        abc=line_input()
    elif mthd == "sep":
        abc=sep_input()
    else:
        print(f"\nseems like you wrote {mthd}, thats not line, sep or exit\n")
     
    if abc == [0, 0, 0]:
        print("\nSeems like there is no equation -_-\n")    # если вдруг на вход подались три нуля
    elif abc[0] == 0:
        a0(abc)
    elif abc[1] == 0:
        b0(abc)
    elif abc[2] == 0:
        c0(abc)
    else:
        roots(abc)