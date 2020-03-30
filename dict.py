phones = ['iPhone Xs', 'Samsung 10s','Xiaomi Mi8']
# "key": value
# product = {
#     "name": "iPhone Xs",
#     "stock": 5,
#     "price": 65000
# }
# print(product)
# print(len(product)) # 3

# элементы словая можно добавлять и изменять, обратившись по названию ключа
# Если такой ключ есть - значение будет обновлено.
#  Если ключа нет - он будет создан

# product["stock"] = 10
# print(product)

# product["memory"] = 64
# # print(product) # в конец добавился еще один ключ 
# # print(product["name"]) # iPhone Xs

# #  "Безопасное" обращение по ключу
# # Если вы обратитесь к ключу, которого не существует, программа выдаст
# # ошибку. Если неизвестно, есть ли ключ в словаре, к нему можно
# #  обратиться через метод .get()

# print(product.get("name")) # iPhone Xs
# print(product.get("discount")) # None
# print(product.get("discount", 10)) # 10 - если такого ключа нет, то вернут 
# #  значчение по умолчанию
# print(product.get("name", "iphone 3G")) # iPhone Xs - ничего не изменилось, т.к. такой
# # ключ есть

# # Удаление элемента
# # С помощью функции del() можно удалить элемент по названию ключа. Если
# # такого нет - будет ошибка

# del product["stock"]
# print(product) # {'name': 'iPhone Xs', 'price': 65000, 'memory': 64}

# Словари и списки можно объединять
# списки и словари можно складывать друг в друга, получая структуры данных,
# которые отражают вашу предметную область

# print(product) # {'name': 'iPhone Xs', 'stock': 5, 'price': 65000}
# product["recomend"] = phones
# 
# print(product)
# {'name': 'iPhone Xs', 'stock': 5, 'price': 65000, 'recomend': ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8']}

# и дальше можно работать с вложенным словарем, как с обычным словарем

# product = {
#     "name": "iPhone Xs",
#     "stock": 5,
#     "price": 65000,
#     "recomend": phones
# }

# print(product["recomend"])
# # ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8']

# print(product["recomend"][1]) # Samsung 

# product["recomend"].append("iPhone 6")
# print(product)
# # {'name': 'iPhone Xs', 'stock': 5, 'price': 65000, 'recomend': ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8', 'iPhone 6']}

# # Список словарей
# # Список словарей часто используется в разработке, например
# # это может быть список товаров

# stock = [
#     {"name": "iPhone Xs Plus", "stock": 24, 'price': 65000, 'recomended': ['iPhone Xs', 'Samsung Galaxy S10']},
#     {"name": "Samsung Galaxy S10", "stock": 8, 'price': 50000, 'discount': 5000},
#     {"name": "Xiaomi Mi8", "stock": 42, 'price': 38000.50}
# ]

# # print(stock)
# print(stock[0])
# # {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65000, 'recomended': ['iPhone Xs', 'Samsung Galaxy S10']}

# # print(stock[0]["name"])
# # iPhone Xs Plus

# # stock[0]["price"] = stock[0]["price"] + 10000
# # можно написать так
# stock[0]["price"] += 10000 
# print(stock[0])
# # {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 75000, 'recomended': ['iPhone Xs', 'Samsung Galaxy S10']}

# print(stock[0]["recomended"][1]) #Samsung Galaxy S10
# print(type(stock)) #<class 'list'>
# print(type(stock[0])) #<class 'dict'>

# Задание
# создайье словарь
city_dict = {"city": "Moscow", "temperature": 20}
# выведите значение ключа "city"
print(city_dict["city"]) # Moscow
# уменьшите значение "temp." на 5
city_dict["temperature"] -= 5
# выведите весь словарь
print(city_dict)
# {'city': 'Moscow', 'temperature': 15}

# задание 
# проерьте есть ли в словаре ключ "country"
print(city_dict.get("country")) # None
# выведжите значение по умолчанию "Россия" для ключа "country"
print(city_dict.get("country", "Russia")) # Russia
# выведите на экран длину словаря
print(len(city_dict)) # 2
print(3.3+4.1==7.4) #False, т.к. 3,3+4,1 не = 7,4 при типе данных float







 
  


