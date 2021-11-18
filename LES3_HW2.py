def user_info(name, surname, year, city, email, phone) :
    return f'{name} {surname} {year} {city} {email} {phone}'

u_name = input("Ваше имя:")
u_surname = input("Ваша фамилия:")
u_year = input("Год рождения:")
u_city = input("Город:")
u_email = input("Email:")
u_phone = input("Телефон:")
user_inf = user_info(name=u_name, surname=u_surname, year=u_year, city=u_city, email=u_email, phone=u_phone)
print(user_inf)