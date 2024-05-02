#2. Работа со списками:

#Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
my_list = ['apple', 'banana', 'orange', 'kiwi']
#Выведите на экран список my_list.
print(my_list)
#Выведите на экран первый и последний элементы списка my_list.
print(my_list[0])
print(my_list[-1])
#Выведите на экран подсписок my_list с третьего до пятого элементов.
print(my_list[2:5])
#Измените значение третьего элемента списка my_list.
my_list[2] = 'grape'
#Выведите на экран измененный список my_list.
print(my_list)

#3. Работа со словарями:
#Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
#Выведите на экран словарь my_dict.
print(my_dict)
#Выведите на экран значение для заданного ключа в my_dict.
print(my_dict.get('orange'))
#Измените значение для заданного ключа или добавьте новый в my_dict.
my_dict.update({'grape': 'виноград'})
#Выведите на экран измененный словарь my_dict.
print(my_dict)
