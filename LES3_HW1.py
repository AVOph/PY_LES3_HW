def div_num (a, b):
        return a / b

a = int(input("Введите первое число :"))
b = int(input("Введите второе число :"))
c = 0
while c > 0:
    if b > 0:
        print(div_num(a, b))
        c += 1
        break
else:
    print("Делить на ноль нельзя!")
    a = int(input("Введите заново первое число :"))
    b = int(input("Введите заново второе число :"))
    print(div_num(a, b))
