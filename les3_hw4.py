def expo_num (x, y):
    if x < 0 :
        return "x не положительное число"
    if y > 0 :
        return "y не отрицательное число"
    else:
        return x**y

x = float(input("Введите положительное число x:"))
y = int(input("Введите целое отрицательное число y:"))
print(expo_num(x, y))

