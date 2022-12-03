# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
            except ValueError:
                print("Это не число. Введи числа!")
    return a


def checkCoordinates(xy):
    if xy[0] > 0 and xy[1] > 0:
        plosk = 1
    elif xy[0] < 0 and xy[1] > 0:
        plosk = 2
    elif xy[0] < 0 and xy[1] < 0:
        plosk = 3
    elif xy[0] > 0 and xy[1] < 0:
        plosk = 4
    elif xy[0] == 0 and xy[1] == 0:
        plosk = " не принадлежит не одной"
    print(f"Точка находится в {plosk} четверти плоскости")


koordinate = inputKoord(2)
checkCoordinates(koordinate)