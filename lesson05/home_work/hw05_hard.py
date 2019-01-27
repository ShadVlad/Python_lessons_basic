# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import re
print("sys.argv = ", sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_namec> - создание директории")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")

def make_dir():
    if not dir_name:
        print(" Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f" Директория {dir_name} создана")
    except FileExistsError:
        print(f" Директория {dir_name} уже существует")


def copy_file():
    if not dir_name:
        print(" Необходимо указать имя копируемого файла")
        return
    if os.name == 'nt':
        # Windows
        filename = dir_name.split('\\')[-1]
        print(filename)
        os.system(f"copy {dir_name} copy_{filename}")
    else:
        # Unix
        filename = dir_name.split('/')[-1]
        os.system(f"copy {dir_name} copy_{filename}")


def remove_file():
    if not dir_name:
        print(" Необходимо указать имя удаляемого файла")
        return
    if os.path.exists(dir_name):
        print(f" Файл {dir_name} существует и будет удален")
        yes_not = input("'y' - удалить, другое - не удалять. ")
        if yes_not == 'y':
            try:
                os.remove(dir_name)
                print(f" Файл {dir_name} удален")
            except Exception:
                print(" Файл занят и не может быть удален")
        else:
            print(f" Удаление файла {dir_name} отменено пользователем")
    else:
        print('Файл не существует')


def change_dir():
    if not dir_name:
        print("необходимо указать путь")
        return
    if os.name == 'nt':
        # Windows
        if re.search('^[A-Z]:', dir_name) is None:
            print('относительный путь')
        else:
            print('абсолютный путь')
        try:
            os.chdir(dir_name)
            #print(os.getcwd())
            full_dir()
        except Exception as error:
            print(error)
    else:
        # Unix
        # filename=dir_name.split('/')[-1]
        if re.search('^/', dir_name) is None:
            print('относительный путь')
        else:
            print('абсолютный путь')
        try:
            os.chdir(dir_name)
            print(os.getcwd())
        except Exception as error:
            print(error)


def full_dir():
    print(" Текущая директория: " + os.getcwd())


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
