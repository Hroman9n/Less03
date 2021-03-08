
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # массив с 10 позициями для подсчета частоты

from_to = list(input("Введите два числа, в диапазоне которых необходимо посчитать частоту: ").split())

### Проверка на количество введенных чисел
if len(from_to) < 2:
    print("\nВведено меньше 2 чисел\n")
elif len(from_to) > 2:
    print("\nВведено больше 2 чисел\n")
else:
    ### основное тело программы ###

    # смотрим что подано на вход и можем ли мы это преобразовать
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
    
    # преобразовываем поданую строку в целочисленный массив и находим его максимум и минимум
    from_to = list(map(int, from_to))
    start = min(from_to)
    end = max(from_to)
    
    # в этом цикле мы идем от меньшего числа к большему, попутно разбивая каждое число на цифры,
    # благодаря чему мы можем подсчитать их частоту. 
    for i in range(start,(end+1)):
        for j in str(i):
            try:
                index = int(j)
                numbers[index] = numbers[index]+1
            except:
                continue
    
    print(f"\nВ диапазоне от {start} до {end} частота чисел следующая:\n")

    for i in range(len(numbers)):
        print(f'число {i} повтораяется {numbers[i]} раз')