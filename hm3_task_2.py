def new_func(name, surname, birthday, city, email, phone):
    print(f"Information about user: name - {name};surname  - {surname}; birthday - {birthday}; city - {city}; email - {email}; phone - {phone}")


user_name = input('Enter name: ')
user_surname = input('Enter surname: ')
user_birthday = input('Enter birthday: ')
user_city = input('Enter city: ')
user_email = input('Enter email: ')
user_phone = int(input('Enter phone: '))

new_func(user_name, user_surname, user_birthday, user_city, user_email, user_phone)
