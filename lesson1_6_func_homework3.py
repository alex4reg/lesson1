# применение decimal()
import decimal
from decimal import Decimal

decimal.getcontext().prec=2


def discounted(price, discount, max_discount = 50): 
    price = (abs(price)) # число по модулю
    discount = (abs(discount))
    max_discount = (abs(max_discount))
    if max_discount > 99:
        raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= max_discount:
        price_with_discount = price
    else:
        # price = Decimal.from_float(price)
        # print(price)
        # discount = Decimal.from_float(discount)
        price_with_discount = Decimal(price-price*discount/100)
    print(price_with_discount)
    return(price_with_discount)

product = {"name": "Samsung Galaxy S10", "stock": 8, 'price': 50000, 'discount': 40.3666}

# 
b = discounted(product['price'], product['discount'], max_discount=71)
product['with_discount'] =  float(b) #discounted(product['price'], product['discount'], max_discount=71)
# 
print(product)
print(Decimal("7").sqrt())

