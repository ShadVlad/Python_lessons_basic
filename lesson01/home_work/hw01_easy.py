
__author__ = 'Владимир Шадрин'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
print("Проограмма выведет цифры введеного Вами целого числа")
number_str = input("Введите целое число: ")
number = int(number_str)
print(number)
print()
# цикл while
while number > 0:
    print(number%10)
    number = number // 10
print()
# цикл for
number_length = len(number_str)
for i in range(number_length):
    print(i + 1,"-я цифра: ", number_str[i])

print()

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print("Программа поменяет значения введеных Вами двух чисел")
number_a = float(input("Введите число A: "))
number_b = float(input("Введите число B: "))
print()
print("Вы вели число А: ", number_a, " и число B:", number_b)
print()

# через арифметические действия
number_a = number_a + number_b
number_b = number_a - number_b
number_a = number_a - number_b
print("А теперь число А = ", number_a, ", а число B = ", number_b)
print()

# решение через дополнительную переменную
number_c = number_a
number_a = number_b
number_b = number_c
print("И снова число А = ", number_a, ", а число B = ", number_b)
print()

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

name_user = input("Как Вас зовут? ")
age_user = int(input(name_user + ", сколько Вам лет? "))

if age_user < 18:
    print('Извините,', name_user, 'пользование данным ресурсом только с 18 лет')
else:
    print(name_user, ', доступ разрешен')

