# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def numInput ():
    num=int(input(""))
    return num

def distances_between_points (a,b):
    d= ((b[1]-a[1])**2+(b[0]-a[0])**2)**0.5
    print(f"A {a}; B {b} -> {round(d,2)}")



print ("Введите значение координаты первой точки X: ")
x=numInput()
print ("Введите значение координаты первой точки Y: ")
y=numInput()

coordinates_first=[x,y]

print ("Введите значение координаты вторй точки X: ")
x=numInput()
print ("Введите значение координаты второй точки Y: ")
y=numInput()

coordinates_second=[x,y]

distances_between_points(coordinates_first,coordinates_second)