### проверка на простое число ###
def simple():

    n=int(input())

    if type(n) != int:
        print("Введенное число не является целым, либо введено не число\n")
        exit()
    elif type(n) == int:

        for i in range(2, n-1):
            if n % i == 0:
                print(f"Число {n} не является простым")
                exit()
        
        print(f"Число {n} является простым")


### нахождение НОК ###
def NOK():
    pass


### нахождение НОД ###
def NOD():
    pass

while(1):

    prog = input("""Чтобы определить является ли число простым наберите 1, чтобы найти НОК наберите 2, 
        чтобы найти НОД наберите 3. Чтобый закончить выполнение программы наберите 'exit': """)

    print()

    if prog == "exit":
        exit()
    elif prog == '1':
        simple()
    elif prog == '2':
        NOK()
    elif prog == '3':
        NOD()
    else:
        print(f"Введены не числа 1, 2, 3, либо exit, вместо этого введено {prog}")

    