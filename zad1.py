# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

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
    if 6 <= num <= 7:
        print("Это выходной день")
    elif 0 < num < 6:
        print("Это будний день")
    else:
        print("в неделе 7 дней напиши число от 1 до 7")


num = InputNumbers("Введите число: ")
checkNumber(num)