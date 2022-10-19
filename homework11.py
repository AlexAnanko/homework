import os
import shutil


def mkdirs():
    os.mkdir("PythonFiles") # Создание новой директории для файлов с расширение .ру
    os.mkdir("TXTFiles") # Создание новой директории для файлов с расширение .txt
    os.mkdir("JsonFiles") # Создание новой директории для файлов с расширение .json
    return "Diectories create is complete"

# def sorted_by_name(): # Перенос копий файлов в соответствующую директорию.
#     files = os.listdir()
#     python_files = [] # Сборочный массив для подсчёта перенесенных файлов в соответствующую директорию
#     txt_files = [] # Сборочный массив для подсчёта перенесенных файлов в соответствующую директорию
#     json_files = [] # Сборочный массив для подсчёта перенесенных файлов в соответствующую директорию
#     p = 0 # Счётчик размера файлов с расширением .py
#     t = 0 # Счётчик размера файлов с расширением .txt
#     j = 0 # Счётчик размера файлов с расширением .json
#     for i in files:
#         if i.endswith(".py"):
#             python_files.append(i) # Запись в соответствующий сборочный массив для подсчёта перенесенных копий файлов
#             shutil.copy2(i, "PythonFiles") # Создание и перенос копии файла в соответствующую директорию
#             p += os.path.getsize(i)
#
#         if i.endswith(".txt"):
#             txt_files.append(i) # Запись в соответствующий сборочный массив для подсчёта перенесенных копий файлов
#             shutil.copy2(i, "TXTFiles") # Создание и перенос копии файла в соответствующую директорию
#             t += os.path.getsize(i)
#         if i.endswith(".json"):
#             json_files.append(i) # Запись в соответствующий сборочный массив для подсчёта перенесенных копий файлов
#             shutil.copy2(i, "JsonFiles") # Создание и перенос копии файла в соответствующую директорию
#             j += os.path.getsize(i)
#     print(f"В папку Python Files перемещено {len(python_files)} файлов, суммарный размер файлов составил {p} байт")
#     print(f"В папку TXT Files перемещено {len(txt_files)} файлов, суммарный размер файлов составил {t} байт")
#     print(f"В папку Json Files перемещено {len(json_files)} файлов, суммарный размер файлов составил {j} байт")
#     return "Общий размер всех файлов составил -", p+t+j

def sorted_by_name_without_copy(): # Перенос файла без копирования.
    try:
        files = os.listdir()
        python_files = [] # Сборочный массив для подсчёта перенесенных файлов в соответствующую директорию
        txt_files = [] # Сборочный массив для подсчёта перенесенных файлов в соответствующую директорию
        json_files = [] # Сборочный массив для подсчёта перенесенных файлов в соответствующую директорию
        p = 0 # Счётчик размера файлов с расширением .py
        t = 0 # Счётчик размера файлов с расширением .txt
        j = 0 # Счётчик размера файлов с расширением .json
        for i in files:
            if i.endswith(".py"):
                p += os.path.getsize(i)
                dest = "PythonFiles/" + i # Конечный путь файла
                os.replace(i, dest) # Перемещение файла в соответствующую директорию
            if i.endswith(".txt"):
                t += os.path.getsize(i)
                dest = "TXTFiles/" + i # Конечный путь файла
                os.replace(i, dest) # Перемещение файла в соответствующую директорию
            if i.endswith(".json"):
                j += os.path.getsize(i)
                dest = "JsonFiles/" + i # Конечный путь файла
                os.replace(i, dest) # Перемещение файла в соответствующую директорию
        print(f"В папку PythonFiles перемещено {len(python_files)} файлов, суммарный размер файлов составил {p} байт")
        print(f"В папку TXTFiles перемещено {len(txt_files)} файлов, суммарный размер файлов составил {t} байт")
        print(f"В папку JsonFiles перемещено {len(json_files)} файлов, суммарный размер файлов составил {j} байт")
        return "Общий размер всех файлов составил -", p+t+j
    except Exception:
        print("The directory or file is already exists")

def startfile():
    f = os.getcwd() + "\PythonFiles\HelloWorld.py"
    print("After start HelloWorld.py file the result is:")
    os.system(f)
    f = os.getcwd() + "\PythonFiles\some_python_file.py"
    print("After start some_python_file.py file the result is:")
    os.system(f)
    f = os.getcwd() + "\PythonFiles\\file.py"
    print("After start some_python_file.py file the result is:")
    os.system(f)
    return "Program is complete"

def rename():
    dir = os.getcwd()
    new_dir = dir.replace("PythonFiles","")
    r = new_dir + "\TXTFiles"
    os.chdir(r)
    os.rename(r + "\\text.txt", r + "\\t.txt")
    os.rename(r + "\\text1.txt", r + "\\t1.txt")
    os.rename(r + "\\text2.txt", r + "\\t2.txt")
    r = new_dir + "\JsonFiles"
    os.rename(r + "\\text.json", r + "\\tt.json")

print("The name of OS -", os.name)
print("The directory is:", os.getcwd())
print(os.listdir())
mkdirs()
print(sorted_by_name_without_copy())
print(startfile())
rename()
