# a="Привет"
# b='мир'
# c = a +' ' + b + "!"
# print (c)

# a="Привет"
# b='мир'
# c = '{} {}!'.format(a, b) # задаем шаблон строки и переменные
# print (c)

# a="Привет"
# b='мир'
# c=2
# d = a +' ' + b + c + "!" #такое не будет работать, т.к. складывать надо один ти тот же тип
# print (d)

# a="Привет"
# b='мир'
# c=2
# c = '{} {}{}!'.format(a, b, c) # преобразует int в str
# print (c)

# user = "Python"
# c = 'Привет {name}!'.format(name=user) 
# print(c)

# fстроки
# user = "Python"
# c = f'Привет {user}!' 
# print(c)

# pyformat.info - сайт про форматирование в питоне

# длина строки
# a = "Привет"
# b = "мир" 
# c = f'{a} {b}!' 
# # print(len(c))
# d = len(c)
# print(d)

# # приведение к заглавным буквам
# a = 'Привет'.upper()
# print(a) # ПРИВЕТ
# b = 'МИР'.lower()
# print(b) #привет
# c = 'learn python'.capitalize()
# print(c) # Python

# # Можно убрать пробелы из начала и конца строки
# a = '      Привет     '
# print(a, len(a)) #длина строки 17
# print(a.strip(), len(a.strip())) # длина строки 6

# # заменяем одну подстроку (один или несколько символов) на другую
# a = "Прив3т т3б3".replace('3', 'e')
# print(a) # 'Привет тебе'
# a = 'ПриветЫ'.replace('ы', '')
# print(a) # 'ПриветЫ' - здесь не сработает, т.к. надо учитывать регистр
# # Ы и ы - разные буквы

# # мы можем объединять методы
# a = "Привет приветЫ".lower().replace('ы','').capitalize()
# print(a)

# # мы можем заменять любые вхождения строк
# a = 'Привет мир!'.replace('мир', 'python')
# print(a)

# разбиение строки в список
# a = "learn.python.ru"
# print(a.split('.')) #['learn', 'python', 'ru']

# # например если нужно подсчитать количество слова в предложении
# a = "Предложение  из нескольких слов   12"
# b = print(a.split(' ')) #можно указать так, но тогда предложения будут разбиваться
# # по одному пробелу
# # и выдаст так ['Предложение', '', 'из', 'нескольких', 'слов', '', '', '12']
# # поэтому укажем так:
# b = a.split()
# print(b) # ['Предложение', 'из', 'нескольких', 'слов', '12']
# print(len(b)) # 5

# # тип данных None == отсутствие данных, например если какая то функция 
# # не вернула значение
# a = None
# b = 0
# print(a is None) #True
# print(b is not None) # True

# Типы переменных
# a = 2
# print(type(a)) # <class 'int'>
# b = "2.0"
# print(type(b)) # <class 'str'>
# c = 2.0
# print(type(c)) # <class 'float'>
# d = True
# print(type(d)) # <class 'bool'>
# f = None 
# print(type(f)) # <class 'NoneType'>

# # ВВод от пользователя
# name = input("Введите ваше имя: ")
# print(f'Привет, {name}!')

# age = input('Сколько вам лет?') # все, что пришло из input Это тип строка
# birth_year = 2020 - age # ошибка
# print(f'Вы родились в {birth_year} году.')

# age = int(input('Сколько вам лет?')) # поэтому ввод преобразуем в тип int
# birth_year = 2020 - age # ошибка
# print(f'Вы родились в {birth_year} году.')

# приведение типов
# функция int() превращает то, что ей дали в целое число, если может
# может преобразовать строку, содержащюю число и float ---> int
# float --> вещественное число
# bool --> в логическое значение, все что не пустое, !=0, !=None в True
print(bool("Привет")) # True
print(bool(2)) # True
print(bool(-0.1)) # True
print(bool(0)) # False
print(bool(None)) # Fasle
print(bool()) # False
print(bool("")) # False
# str --> что угодно в строку
a = "2.0" # строка
b = float(a) # вещественное
print(type(b)) # <class 'float'>
