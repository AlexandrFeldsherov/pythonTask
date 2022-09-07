# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(num):
    num_new=[]
    i = 0
    while i<num:
        x=(int(input(f"Введите значение num [{i}] : ")))
        num_new.insert(i, x)
        i+=1
    return num_new


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)
print(statement)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
