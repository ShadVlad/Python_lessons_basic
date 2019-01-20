import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("\n    -= Задание 1 =-")
print("Числа Фибоначчи из заданного интервала")


def fibonacci(n, m):
    fibo_list = []
    i = 2
    a = 1
    b = 1
    if n == 1:
        fibo_list.append(1)

    while i <= m:
        a, b = b, a + b
        if i >= n:
            fibo_list.append(a)
        i += 1

    return fibo_list


print(fibonacci(10, 19))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("\n    -= Задание 2 =-")
print("Сортировка списка по возрастанию")


def sort_to_max(origin_list):
    copy_list = origin_list
    length_list = len(copy_list)
    for i in range(length_list - 1):                                # пузырьковая сортировка наоборот
        for j in range(i + 1, length_list):
            if copy_list[j] < copy_list[i]:
                copy_list[j], copy_list[i] = copy_list[i], copy_list[j]

    print(copy_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print("\n    -= Задание 3 =-")
print("Аналог встроенной функции filter()")


def func(x):
    out = []
    for elem in x:
        if elem > 0:
            out.append(elem)
    return out


def my_filter(f, x):
    return f(x)


print(list(my_filter(func, [2, 10, -12, 2.5, 20, -11, 4, 4, 0])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("\n    -= Задание 4 =-")
print("Проверка четырехугольника")


def dist(a, b):
    return math.hypot(b[0] - a[0], b[1] - a[1])


a1 = [1, 2]
a2 = [1, 6]
a3 = [4, 3]
a4 = [4, 7]
print(a1, a2, a3, a4)
print((dist(a1, a2) == dist(a3, a4)) and ((dist(a2, a3) == dist(a1, a4)) or (dist(a1, a3) == dist(a2, a4))))
