# def int_func(text):
#     word = text[0].upper() + text[1:]
#     return word
# user_word = input("Введите слово маленькими латинскими буквами :")
# print(int_func(user_word))

def int_func(text):
    word = text[0].upper() + text[1:]
    return word
user_words = input("Введите слова маленькими буквами через пробел :")
for word in user_words.split(" "):
    print(f'{int_func(word)}', end=" ")
