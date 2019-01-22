# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print("\n    -= Задание 1 =-")
print("Генератор списка квадратов исходного")
lst = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print("Исходный: ", lst)

lst_gen = [el**2 for el in lst]
print("Квадраты: ", lst_gen)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('    -= Задача-2 =-\n')
fruits = ["яблоко", "апельсин",'слива',"банан", "грейпфрут", "киви", "арбуз", "мандарин"]
citruss = ["апельсин", "лайм", "грейпфрут", "мандарин", "клементин" ]
print('fruits: ',fruits)
print('citrus: ',citruss,'\n')

assorti = [fruit for fruit in fruits if fruit in citruss]
print('assorti: ', assorti,'\n')


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('    -= Задача-3 =-\n')
numbers = [2, 10, -12, 15, 20, -9, 4, 6, 0]
print(numbers)
numbers_gen = [el for el in numbers if int(el) % 3 == 0 and int(el) > 0 and int(el) % 4 != 0]
print(numbers_gen)