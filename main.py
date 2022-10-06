# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов
#
# array = "Ivanov Ivan - 3\nPetrov Pavel - 2\nSidorov Vasia - 3\nAlexeev Dmitriy - 5\nShishkin Ivan - 4\nPetrov Ivan - 1\nPopov Dmitriy - 1\nSemenov Sasha - 2"
# with open('class_journal.txt', 'w') as f:
#     f.write(array)
#
# with open('class_journal.txt', 'r') as f:
#     for line in f.readlines():
#         classmates = line.split(' ')
#         n = 3
#         for c in classmates:
#             if c.endswith("\n"):
#                 c.replace("\n", '')
#             if c < str(n) and c != "-":
#                 print(line)

# arr = [
#
#     {"name" : "Ivanov Ivan", "score" : "3"},
#     {"name" : "Petrov Pavel", "score" : "2"},
#     {"name" : "Sidorov Vasia", "score" : "3"},
#     {"name" : "Alexeev Dmitriy", "score" : "5"},
#     {"name" : "Shishkin Ivan", "score" : "4"},
#     {"name" : "Petrov Ivan", "score" : "1"},
#     {"name" : "Popov Dmitriy", "score" : "1"},
#     {"name" : "Semenov Sasha", "score" : "2"}
#
# ]

# with open('class_journal.json', 'w') as f:
#     json.dump(arr, f, indent=3)
#
# with open('class_journal.json', 'r') as f:
#     json.load(f)
#     n = str(input("Введите оценку: "))
#     for i in arr:
#         if n > i.get("score"):
#             print(i)

# В файле могут быть записаны десятичные цифры и все, что угодно.
# Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно).
#
# Вычислите сумму всех чисел, записанных в файле. В данной задаче удобно считывать данные посимвольно.

with open('summa_chisel.txt', 'w') as f:
    f.write("123nnweov\n4pq5le\n1qpw6l\n4 5 6 7 8 9\nqk27fpwqk4lom3")

alpha = []
num = []
numbers = ""

with open('summa_chisel.txt', 'r') as f:
    for line in f:
        summa = 0
        for i in line:
            i.split(" ")
            if i.endswith("\n"):
                i.replace("\n", "")
            elif not i.isalpha():
                i.replace(i," ")
                # print(i, end="")
                num.append(i)
            # else:
            #     print(" ", end="")
                # alpha.append(i)
    print(num)
    print(numbers)
    #print(summa)