import os

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("\n    -= Задание 1 =-")
print("Операции с дробями")

equation = input("Введите выражение: ")
equation_items = equation.split(' ')
print(equation_items)
number_s = equation_items[0].find('/')
if number_s > 0:
    b = int(equation_items[0][number_s + 1:])
    a = int(equation_items[0][: number_s])
else:
    a = int(equation_items[0])
    b = 1

number_s = equation_items[2].find('/')
if number_s > 0:
    d = int(equation_items[2][number_s + 1:])
    c = int(equation_items[2][: number_s])
else:
    c = int(equation_items[2])
    d = 1

if equation_items[1] == '-':
    c = - c

result_num = a * d + c * b
result_denom = b * d

integer_part = result_num // result_denom
numerator = result_num % result_denom
print(f'{integer_part} {numerator}/{result_denom}')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("\n    -= Задание 3 =-")
print("Работа с файлами fruits")

rus_caps = list(map(chr, range(ord('А'), ord('Я')+1)))
DIR = "data"
litera = ''
name_f = ''
with open(os.path.join(DIR, 'fruits.txt'), 'r', encoding='UTF-8') as f:
    for line in f:  # считываем файл построчно
        litera_old = litera
        litera = line[0]
        if litera in rus_caps:
            if litera_old != litera:
                name_f = "fruits_" + litera + ".txt"
            with open(os.path.join(DIR, name_f), 'a+', encoding='UTF-8') as f1:
                f1.writelines(line)

print("Готово!")
