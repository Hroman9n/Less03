
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # массив с 10 позициями для подсчета частоты

from_to = list(input("Введите два числа, в диапазоне которых необходимо посчитать частоту: ").split())

### Проверка на количество введенных чисел
if len(from_to) < 2:
    print("\nВведено меньше 2 чисел\n")
elif len(from_to) > 2:
    print("\nВведено больше 2 чисел\n")
else:
    ### основное тело программы
    try:
        int(from_to[0])
    except ValueError:
        print(f"\nПервое значение не является целым числом или вовсе не является числом ({from_to[0]})\n")
        exit()
    
    try:
        int(from_to[1])
    except ValueError:
        print(f"\nВторое значение не является целым числом или вовсе не является числом ({from_to[1]})\n")
        exit()
    
    from_to = list(map(int, from_to))
    start = min(from_to)
    end = max(from_to)
    
    for i in range(start,(end+1)):
        for j in str(i):
            index = int(j)
            numbers[index] = numbers[index]+1
    
    print(f"\nВ диапазоне от {start} до {end} частота чисел следующая:\n")

    for i in range(len(numbers)):
        print(f'число {i} повтораяется {numbers[i]} раз\n')