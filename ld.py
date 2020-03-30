# phones = ['iPhone Xs', 'Samsung 10s','Xiaomi Mi8']

# print(phones)

# phones_count = len(phones)
# print(phones_count)

# phones.append("iPhone 6") #добавить элемент, в конец списка
# print(phones)

# # подсчитать количество элементов в списке
# print(phones.count("iPhone Xs")) #1
# print(phones.count("iPhone 9")) # 0 - нет такого элемента

#индексы считаются с 0 и идут последовательно
# print (phones[1]) #Samsung 10s, если указать индекс, которого нет, 
# # то выдаст ошибку

# # Срезы - получить часть списка, последний индекс "3" не включительно
# #
# print(phones[1:3]) #['Samsung 10s', 'Xiaomi Mi8']

# print(phones[-1]) #Xiaomi Mi8 - получить посдедний элемент списка

# print(phones[:2]) #['iPhone Xs', 'Samsung 10s']
# #  - получить элементы с 0 по 2 не включительно

#Поиск элементов
# print(phones.index("Samsung 10s")) #1

# #сортировка, не сработает, если есть разные типы данных
# phones = ['iPhone Xs','Xiaomi Mi8','Samsung 10s']
# phones.sort()
# print(phones) #['Samsung 10s', 'Xiaomi Mi8', 'iPhone Xs']
# #сначала слотируется по заглавным буквам, потом по строчным

# # Оператор in

# print("Samsung 10s" in phones) #True - проверяет точное совпадение,
#  samsung 10s - вернет False

# # Удаление элементов
# phones = ['iPhone Xs','Xiaomi Mi8','Samsung 10s','iPhone Xs']

# print(phones)
# # del phones[3] # удаление по индексу
# # print(phones) #['iPhone Xs', 'Xiaomi Mi8', 'Samsung 10s']
# phones.remove("iPhone Xs") # удалит первый элемент, который встретился первым
# # с таким названием
# print(phones) #['Xiaomi Mi8', 'Samsung 10s', 'iPhone Xs']

# Задание

# Создайте список из чисел 3, 5, 7, 9, 10.5
work_list=[3, 5, 7, 9, 10.5]
# Выведите содержимое на экран
print(work_list)
# Добавьте в конец списка строку "Python"
work_list.append("Python")
# Выведите длину списка на экран
print(work_list) #[3, 5, 7, 9, 10.5, 'Python']
print(len (work_list)) #6
# Выведите на экран начальный элемент списка
print(work_list[0]) #3
# Выведите на экран последний
print(work_list[-1]) # Python - смотри выведл без кавычек
# Напечатайте элементы со втрого по четверый включительно
print(work_list[2:5]) #[7, 9, 10.5]
# Удалите из списка строку "Python"
work_list.remove('Python')
print(work_list) #[3, 5, 7, 9, 10.5]