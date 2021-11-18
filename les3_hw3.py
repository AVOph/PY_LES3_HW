def sum_max_func(num_1, num_2, num_3):
    a=[num_1, num_2, num_3]
    return sum(a) - min(a)
user_num_1 = int(input("Введите первое число:"))
user_num_2 = int(input("Введите второе число:"))
user_num_3 = int(input("Введите третье число:"))
my_func = sum_max_func(user_num_1, user_num_2, user_num_3)
print(my_func)