def sum_num(user_nums, stop_word):
    num_list = user_nums.split(' ')
    sum_num_list = 0
    for i in num_list:
        if i == stop_word:
            break
        sum_num_list += int(i)
    return sum_num_list

u_stop_word = "!"
finish = 0
b = 0
while finish == 0 :
    user_all_nums = input("Введите числа через пробел :")
    b += sum_num(user_all_nums, u_stop_word)
    if u_stop_word in user_all_nums:
        finish +=1
        print(f' Сумма = {b}')
        break
    print(f' Сумма = {b}')



