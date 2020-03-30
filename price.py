# price = 100
# discount = 5

# print_with_discount = price - price*discount/100
# print(print_with_discount)

# def discounted(price, discount):
#     print_with_discount = price - (price*discount/100)
#     print(print_with_discount)

# discounted(111, 3.5)

# Усложним фукнцию, добавив проверку
# def discounted(price, discount):
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price*discount/100)
#     print(price_with_discount)

# price2 = 100
# discount2 = 180
# discounted(price2, discount2)

# используем abs() чтобы цена и скидка были положительными

# def discounted(price, discount):
#     price = abs(float(price)) # число по модулю
#     discount = abs(float(discount))
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price*discount/100)
#     # print(price_with_discount)
#     return(price_with_discount)

# # price2 = -100
# # discount2 = -18
# # discounted(price2, discount2)

# # Эта функция - просто пример. Есть два важных момента, почему эту функцию
# # нельзя использовать в реальных проектах:
# #  - нельзя делать приведение типов, например float() без проверки
# # исключений. Вам могут подать на вход функции не число, и ваша
# # программа сломается
# # - тип float не подходит для представления цен, т.к. очень вольно
# # обходится с правилами округления. Если вы хотите работь с ценами,
# # почитайте про Decimal
# # discounted("Fuck", [1,2,3 ]) # выдаст ошибку

# # p = discounted(100, 10) 
# # print(p)

# product = {"name": "Samsung Galaxy S10", "stock": 8, 'price': 50000, 'discount': 50}
# product['with_discount'] = discounted(product['price'], product['discount'])
# print(product)

# # discounted(price, discount) - позиционные аргументы, строгий порядок и количество
# # именованные аргументы
# # помимо обязательных позиционных аргументов, мы можем задать
# # необязательные именованные. Они отличаются тем, что у них есть
# # значения по умолчанию
# # например, можно дать возможность управлять максимальной скидкой

def discounted(price, discount, max_discount = 50): # заменяем максимальную скидку на аргумент по умолчаниию 
    price = abs(float(price)) # число по модулю
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price*discount/100)
    # print(price_with_discount)
    return(price_with_discount)

product = {"name": "Samsung Galaxy S10", "stock": 8, 'price': 50000, 'discount': 70}
# {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000, 'discount': 40, 'with_discount': 30000.0}
# цена изменилась

# product['with_discount'] = discounted(product['price'], product['discount'])
product['with_discount'] = discounted(product['price'], product['discount'], max_discount=71)
# если не передаем именнованный аргумент, то будет исользоваться значение по умолчанию
print(product)

# discounted(100, 50, 100)
# или так можно вызвать
# discounted(100, 50, max_discount = 100)
# C:\projects\lesson1>price.py
# {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000, 'discount': 70, 'with_discount': 50000.0}
# Traceback (most recent call last):
#   File "C:\projects\lesson1\price.py", line 87, in <module>
#     discounted(100, 50, 100)
#   File "C:\projects\lesson1\price.py", line 70, in discounted
#     raise ValueError("Максимальная скидка не может быть больше 99%")
# ValueError: Максимальная скидка не может быть больше 99%
print( discounted(100, 50, max_discount = 71))
# 50.0 - 50< 71 --> 100*0,5=50




