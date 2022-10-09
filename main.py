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
#
# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:
#  • метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False в зависимости от того,
#  может ли текущая строку быть получена целым количеством повторов строки s. Вернуть False, если s не является строкой.
#  Считать, что пустая строка не содержит повторов.
#  • метод is_palindrom (), который возвращает True или False в зависимости от того, является ли строка палиндромом.
#  Регистрами символов пренебрегать. Пустую строку считать палиндромом.

# class SuperStr(str):
#     def __init__(self, s):
#         self.s = s
#
#     def is_repeatance(self, s):
#         if s == "" or s == " " or not isinstance(s, str): # Проверяет принадлежит ли то что в s объекту типа str
#             return False
#         else:
#             n = len(self) // len(s)
#             return self == n * s
#
#     def is_palindrom(self):
#         s = self.lower()
#         return s == s[::-1]
#
#
# S = SuperStr("sabsabsabsab")
# print(S.is_repeatance("sabsab"))
# S1 = SuperStr("123321")
# print(S1.is_palindrom())

# В файле могут быть записаны десятичные цифры и все, что угодно.
# Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно).
#
# Вычислите сумму всех чисел, записанных в файле. В данной задаче удобно считывать данные посимвольно.
#
# line = "123nnweov\n4pq5le\n1qpw6l\n4 5 6 7 8 9\nqk27fpwqk4lom35jj676h"
# with open('summa_chisel.txt', 'w') as f:
#     f.write(line)
#
# with open('summa_chisel.txt', 'r') as f:
#     i = 0
#     numbers = []
#     number = ""
#     new_numbers = []
#     while i < len(line):
#         if line[i].isdigit():
#             number += line[i]
#         elif numbers != '':
#             numbers.append(number)
#             number = ''
#         i += 1
#         for n in numbers:
#             if n == '':
#                 numbers.remove(n)
#     for e in numbers:
#         new_numbers.append(int(e))
#     summa = 0
#     for n in new_numbers:
#         summa += n
#
# print(new_numbers)
# print(summa)

# В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам.
# Каждый избиратель указывает одну партию, за которую он отдает свой голос.
# В Государственную Думу попадают партии, которые набрали не менее 7% от числа голосов избирателей.
#
# Дан список партий и список голосов избирателей. Выведите список партий, которые попадут в Государственную Думу.
#
# Входные данные
# В первой строке входного файла написано слово PARTIES:. Далее идет список партий, участвующих в выборах.
#
# Затем идет строка, содержащая слово VOTES:.
# За ней идут названия партий, за которые проголосовали избиратели,
# по одному названию в строке. Названия могут быть только строками из первого списка.
#
# Выходные данные
# Программа должна вывести названия партий, получивших не менее 7% от числа голосов в том порядке,
# в котором они следуют в первом списке.
#
# line = "PARTIES:\nParty one\nParty two\nParty three\nVOTES:\nParty one\nParty one\nParty three\nParty one\nParty one\nParty three\nParty two\nParty one\nParty three\nParty three\nParty one\nParty one\nParty three\nParty three\nParty one"
#
# with open('parties.txt', 'w') as f:
#     f.write(line)
#
# with open('parties.txt','r+') as f:
#     file_reader = f.read().splitlines()
#     for i in file_reader:
#         party_one = file_reader[4::].count("Party one")
#         party_two = file_reader[4::].count("Party two")
#         party_three = file_reader[4::].count("Party three")
#     counts = party_one + party_two + party_three
#     if ((party_one / counts) * 100) > 7:
#         print("Party one")
#     if ((party_two / counts) * 100) > 7:
#         print("Party two")
#     if ((party_three / counts) * 100) > 7:
#         print("Party three")


# Q: Выборы Государственной Думы
#
# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации”
# определяет следующий алгоритм пропорционального распределения мест в парламенте.
#
# Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей,
# поданных за каждую партию и подсчитывается сумма голосов, поданных за все партии.
# Эта сумма делится на 450, получается величина, называемая “первое избирательное частное”
# (смысл первого избирательного частного - это количество голосов избирателей,
# которое необходимо набрать для получения одного места в парламенте).
#
# Далее каждая партия получает столько мест в парламенте,
# чему равна целая часть от деления числа голосов за данную партию на первое избирательное частное.
#
# Если после первого раунда распределения мест сумма количества мест,
# отданных партиям, меньше 450, то оставшиеся места передаются по одному партиям,
# в порядке убывания дробной части частного от деления числа голосов за данную партию на первое избирательное частное.
# Если же для двух партий эти дробные части равны, то преимущество отдается той партии,
# которая получила большее число голосов.
#
# На вход программе подается список партий, участвовавших в выборах.
# Каждая строка входного файла содержит название партии (строка, возможно, содержащая пробелы),
# затем, через пробел, количество голосов, полученных данной партией – число, не превосходящее 108.
#
# Программа должна вывести названия всех партий и количество голосов в парламенте,
# полученных данной партией. Названия необходимо выводить в том же порядке, в котором они шли во входных данных.

# line = "Party One 100000\nParty Two 200000\nParty Three 400000"
# with open('parties(votes).txt', 'w') as f:
#     f.write(line)
#
# with open('parties(votes).txt', 'r+') as f:
#     file_reader = f.read().split()
#     votes = list()
#     v = (file_reader[2:len(file_reader):3])
#     for i in v:
#         votes.append(int(i))
#     summa = 0
#     for i in votes:
#         summa += i
#     first_vote_law = summa // 450
#     party_one = votes[0] / first_vote_law
#     party_two = votes[1] / first_vote_law
#     party_three = votes[2] / first_vote_law
#     counts = party_one + party_two + party_three
#     if counts < 450:
#         if party_one % 1 < party_two % 1:
#             party_two += 1
#         elif party_two % 1 < party_three % 1:
#             party_three += 1
#     print(round(party_one))
#     print(round(party_two))
#     print(round(party_three))
