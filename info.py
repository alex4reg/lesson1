name=input("Введите ваше имя: ").lower().capitalize()
surname=input("Введите вашу фамилию: ").lower().capitalize()
user_info={"first_name": name, "last_name": surname}
print(user_info["first_name"])
print(f'Ваше блятское имя: {user_info["first_name"]}')

