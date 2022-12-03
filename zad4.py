# апишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkNumber(num):
    if num == 1:
        x = list(range(1, 15))
        y = list(range(1, 15))
        print("X в этой плоскости = ", x)
        print("Y в этой плоскости = ", y)
    elif num == 2:
        x = list(range(-15, 0))
        y = list(range(1, 15))
        print("X в этой плоскости = ", x)
        print("Y в этой плоскости = ", y)
        print("Это будний день")
    elif num == 3:
        x = list(range(-15, 0))
        y = list(range(-15, 0))
        print("X в этой плоскости = ", x)
        print("Y в этой плоскости = ", y)
    elif num == 4:
        x = list(range(1, 15))
        y = list(range(-15, 0))
        print("X в этой плоскости = ", x)
        print("Y в этой плоскости = ", y)
    else:
        print("в неделе 7 дней, напиши число от 1 до 7")


num = InputNumbers("Введите число: ")
checkNumber(num)