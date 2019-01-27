# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil


def make_dirs(dir_name):                                    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,

    for name in dir_name:
        dir_path = os.path.join(os.getcwd(), name)
        try:
            os.mkdir(dir_path)
            print(f'директория {dir_path} создана')
        except FileExistsError:
            print(f'директория {dir_path} уже существует')


# Вызов функции
def remove_dirs(dir_name):                                  # И второй скрипт, удаляющий эти папки.
    for file in dir_name:
        if os.path.isdir(file):
            try:
                os.rmdir(file)
                print(f'директория {file} удалена')
            except FileNotFoundError:
                print(f'директория {file} не существует')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir(only_dir = False):
    for _ in os.listdir(os.getcwd()):
        if only_dir:
            if os.path.isdir(_):
                print(_)
        else:
            print(_)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_execute_file():
    file_name = os.path.basename(sys.argv[0])
    copy_name = 'copy_' + file_name
    shutil.copy(file_name, copy_name)




if __name__ == "__main__":
    dir_lists = ['dir_' + str(i) for i in range(1, 10)]
    make_dirs(dir_lists)
    list_dir(True)
    list_dir()
    remove_dirs(dir_lists)
    print(os.listdir(os.getcwd()))
    copy_execute_file()
    print(os.listdir(os.getcwd()))


