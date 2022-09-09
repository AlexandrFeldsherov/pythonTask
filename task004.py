# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def check_input ():
    num=int(input('Введите номер четверти координат: '))
    while num<1 or num>4:
        print("Неверное обозначение четверти, возможно только от 1 до 4")
        num=check_input()
    return num

def range_coordinates(value):
    if value == 1:
        print(f'для {value} четверти -> x > 0; y > 0')
    elif value == 2:
        print(f'для {value} четверти -> x < 0; y > 0')
    elif value == 3:
        print(f'для {value} четверти -> x < 0; y < 0')
    elif value == 4:
        print(f'для {value} четверти -> x > 0; y < 0')
   

quarter_coordinates = check_input()
range_coordinates(quarter_coordinates)
