# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("\n    -= Задание 1 =-")


def my_round(number, ndigits):
    str_number = str(number)
    integer_part, fractional_part = str_number.split('.')
    if ndigits >= len(fractional_part):
        return float(number)
    last_digit = fractional_part[ndigits]
    fractional = fractional_part[:ndigits]
    if int(last_digit) < 5:
        return float(integer_part + '.' + fractional)
    else:
        str_numb = integer_part + fractional
        str_digits = ''
        i = len(str_numb)
        order = True
        for digit in reversed(str_numb):
            i -= 1
            if digit == '9':
                str_digits = '0' + str_digits
                order = True
            else:
                if order:
                    str_digits = str(int(digit) + 1) + str_digits
                    order = False
                    str_digits = str_numb[: i] + str_digits
                    break
                else:
                    str_digits = digit + str_digits

        if order:
            str_digits = '1' + str_digits

        return float(str_digits[: -ndigits] + '.' + str_digits[-ndigits:])


print(my_round(2.1234547, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(1899.9999967, 6))
print(my_round(999.9999967, 7))
print(my_round(999.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("\n    -= Задание 2 =-")


def lucky_ticket(ticket_number):
    str_number = str(ticket_number)
    len_number = len(str_number)
    if len_number % 2 == 0:
        len_half = len_number // 2
        return sum(map(int, str_number[:len_half])) == sum(map(int, str_number[len_half:]))
    else:
        return False


print(lucky_ticket(123006))    # счастливый
print(lucky_ticket(12321))     # не счастливый
print(lucky_ticket(436751))    # счастливый
print(lucky_ticket(416751))    # не счастливый
