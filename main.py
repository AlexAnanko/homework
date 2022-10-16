from math import tan, degrees

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

# Класс "ПчёлоСлон"(BeeElephant)
#
#  Экземпляр класса инициализируется двумя целыми числами: первое относится к пчеле, второе - к слону.
# Класс реализует следующие методы:
# - fly() - может летать - возвращает True,если часть пчелы не меньше части слона, иначе False.
# - еtrumpet() - трубить - если часть слона не мегьше части пчелы, возвращает строку "tu-tu-doo-doo!", иначе "wzzzzz"
# - eat(meal, value) - есть - может есть только нектар(nectar) или траву(grass). Если съедает нектар, то из части слона
# вычитается количество съеденного, пчеле добавляется, иначе наоборот. Не может увеличится больше 100 и уменьшится
# меньше 0.
# -get_parts() - возвращает список из значений.

# class BeeElephant:
#
#     def __init__(self, bee, elephant):
#         self.bee = bee
#         self.elephant = elephant
#
#     def fly(self):
#         if self.bee > self.elephant:
#             return True
#         else:
#             return False
#
#     def trumpet(self):
#         if self.bee < self.elephant:
#             return "tu-tu-doo-doo!"
#         else:
#             return "wzzzzz"
#
#     def eat(self, meal, value):
#         if meal == "nectar":
#             self.bee = self.bee + value
#             if self.bee > 100:
#                 self.bee = 100
#             self.elephant = self.elephant - value
#             if self.elephant < 100:
#                 self.elephant = 0
#             return self.bee, self.elephant
#         else:
#             self.bee = self.bee - value
#             if self.bee < 0:
#                 self.bee = 0
#             self.elephant = self.elephant + value
#             if self.elephant > 100:
#                 self.elephant = 100
#             return self.bee, self.elephant
#
#     def get_parts(self):
#         return self.bee, self.elephant
#
# be = BeeElephant(3,2)
# print(be.fly())
# print(be.trumpet())
# be.eat("grass", 4)
# print(be.get_parts())
# print("==================")
# be1 = BeeElephant(13,87)
# print(be1.fly())
# print(be1.trumpet())
# be1.eat("nectar", 90)
# print(be1.get_parts())
#
# Класс "Прямоугольный треугольник"
#
# Класс содержит два действительных числа - стороны треугольника и включает следующие методы:
# - увеличение/уменьшение размера стороны на заданное количество процентов;
# - вычисление радиуса описанной окружности;
# - вычисление периметра;
# - определение значений углов
#
# class Triangle:
#
#     def __init__(self, a : int, b : int):
#         self.a = a
#         self.b = b
#
#     def percent_change_increase(self, persent):
#         return self.a * ((persent + 100) / 100), self.b * ((persent + 100) / 100)
#
#     def percent_change_decrease(self, persent):
#         return round(self.a / ((persent + 100) / 100),4), round(self.b / ((persent + 100) / 100), 4)
#
#     def radius_circle(self):
#         c = (self.a ** 2 + self.b ** 2) ** (0.5)
#         s = (self.a * self.b) / 2
#         radius = (self.a * self.b * c) / (4 * s)
#         return round(radius, 4)
#
#     def perimeter(self):
#         c = (self.a ** 2 + self.b ** 2) ** (0.5)
#         perimeter = self.a + self.b + c
#         return round(perimeter, 4)
#
#     def angles(self):
#         alpha = degrees(tan(self.a / self.b))
#         betta = 90 - alpha
#         return round(alpha, 4), round(betta, 4)
#
# t = Triangle(2,4)
# print(t.percent_change_increase(30))
# print(t.percent_change_decrease(30))
# print(t.radius_circle())
# print(t.perimeter())
# print(t.angles())
#
# Класс "Автобус"
#
# Класс содержит свойства:
# - speed(скорость);
# - capacity(максимальную вместимость);
# - maxSpeed(максимальную скорость);
# - passengers(список имен пассажиров);
# - hasEmptySeats(наличие свободных мест);
# - seats(словарь мест в автобусе);
# методы:
# - посадка и высадка одного или нескольких пассажиров;
# - увеличение и уменьшение скорости на заданное значение;
# - операции "in", "+=", "-="(посадка и высадка пассажира(ов) с заданной фамилией.
#
# class Bus:
#
#     def __init__(self, speed, capacity):
#         self.speed = speed
#         self.capacity = capacity
#         self.maxSpeed = 50
#         self.passengers = ["Alex", "Dave", "Bob", "Jane"]
#         self.seats = {"Alex" : "1", "Dave" : "2", "Bob" : "3","Jane" : "4"}
#         self.hasEmptySeats = (self.capacity - 2) - len(self.seats)
#
#     def passenger_in(self, n):
#         if len(self.passengers) + n < self.capacity:
#             return f"{n} пассажиров зашло в автобус, количество пассажиров {len(self.passengers) + n}"
#         else:
#             return "Автобус переполнен"
#
#     def passenger_out(self, n):
#         if len(self.passengers) - n > 0:
#             return f"{n} пассажиров вышло из автобуса, количество пассажиров {len(self.passengers) - n}"
#         else:
#             return "Автобус пуст"
#
#     def speed_increase(self, km):
#         if self.speed + km > self.maxSpeed:
#             return self.maxSpeed
#         else:
#             return self.speed + km
#
#     def speed_decrease(self, km):
#         if self.speed - km < 0:
#             return "Автобус остановился"
#         else:
#             return self.speed - km
#
#     def passenger_name_in(self,passenger):
#         if len(self.passengers) < self.capacity:
#             self.passengers.append(passenger)
#             if self.hasEmptySeats > 0:
#                 self.seats[passenger] = str(len(self.seats) + 1)
#             return self.passengers, self.seats, self.hasEmptySeats
#         else:
#             return "Автобус переполнен"
#
#     def passenger_name_out(self, passenger):
#         if passenger in self.passengers:
#             self.passengers.remove(passenger)
#             if passenger in self.seats:
#                 del self.seats[passenger]
#             return self.passengers, self.seats
#         else:
#             return "Такого пассажира не числится"
#
# b = Bus(40, 8)
# print(b.passenger_in(1))
# print(b.passenger_out(1))
# print(b.speed_increase(5))
# print(b.speed_decrease(5))
# print(b.passenger_name_in("Tom"))
# print(b.passenger_name_out("Bob"))

import random

# Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Перемножить элементы каждого столбца матрицы с соответствующими элементами Кго столбца.

# N = 4
# M = 6
#
# matrix = []
# new_matrix = []
# k = []
# for i in range(0,M):
#     matrix.append([])
#     for j in range(0,N):
#         n = random.randint(0,10)
#         matrix[i].append(n)
#         if j == 2:
#             k.append(matrix[i][j])
#     print(matrix[i])
# print("-------------------------")
# for i in range(0,M):
#     new_matrix.append([])
#     for j in range(0,N):
#         m = matrix[i][j] * k[i]
#         new_matrix[i].append(m)
#     print(new_matrix[i])
# print("\n", k)

# Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Просуммировать элементы каждой строки матрицы с соответствующими элементами L той строки.

# N = 6
# M = 5
#
# matrix = []
# new_matrix = []
# L = []
# for i in range(0,M):
#     matrix.append([])
#     for j in range(0,N):
#         n = random.randint(0,10)
#         matrix[i].append(n)
#         if i == 2:
#             L.append(matrix[i][j])
#     print(matrix[i])
# print("----------------------------")
# for i in range(0,M):
#     new_matrix.append([])
#     for j in range(0,N):
#         n = matrix[i][j] + L[j]
#         new_matrix[i].append(n)
#     print(new_matrix[i])
# print("\n",L)

# Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Все элементы имеют целый тип. Дано целое число Н.
# Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.
#
# N = 7
# M = 5
#
# matrix = []
# J = []
# str_J = ""
# H = int(input("Введите искомое число: "))
# for i in range(0,M):
#     matrix.append([])
#     for j in range(0,N):
#         n = random.randint(0,10)
#         matrix[i].append(n)
#         c = matrix[i].count(H)
#     print(matrix[i])
# print("-------------------")
# for j in range(0,N):
#     for i in range(0,M):
#         if matrix[i][j] == H:
#             J.append(j)
# for i in J:
#     k = J.count(i)
#     if k > 1:
#         J.remove(i)
#
# str_J = ", ".join(str(i) for i in J)
#
# print("\nИскомое число =", H)
# if len(J) == 0:
#     print("Такого числа в массиве не найдено.")
# else:
#     print(f"Искомое число встречается в следующих столбцах массива: {str_J}")

# Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
# Исходная матрица состоит из нулей и единиц.
# Добавить к матрице еще один столбец, каждый элемент которого делает количество единиц в каждой строке четным.

# N = 8
# M = 7
#
# matrix = []
#
# h = 1
# L = []
# for i in range(0,M):
#     matrix.append([])
#     for j in range(0,N):
#         n = random.randint(0,1)
#         matrix[i].append(n)
# for i in range(0,M):
#     for j in range(0,N):
#         matrix[i].count(h)
#     if matrix[i].count(h) % 2 != 0:
#         L.append(1)
#     else:
#         L.append(0)
#     print(matrix[i], L[i])


# Класс "Темы" (Themes)
#
# Экземпляру класса при инициализации передается аргумент - список тем для разговора.
# Класс реализует методы:
# - add_theme(value) - добавить тему в конец;
# - shift_one() - сдвинуть темы на одну вправо (последняя становится первой, остальные сдвигаются);
# - reverse_order() - поменять порядок тем на обратный;
# - get_themes() - возвращает список тем;
# - get_first() - возвращает первую тему.
#
# class Themes:
#
#     def __init__(self, themes : list):
#         self.themes = themes
#
#     def add_theme(self, value):
#         return self.themes.append(value)
#
#     def shift_one(self):
#         self.themes.insert(0, self.themes[-1])
#         self.themes.pop(-1)
#         return self.themes
#
#     def reverse_order(self):
#         return self.themes.reverse()
#
#     def get_themes(self):
#         return self.themes
#
#     def get_first(self):
#         return self.themes[0]
#
# # t1 = Themes(['weather', 'rain'])
# # t1.add_theme('warm')
# # print(t1.get_themes())
# # print(t1.shift_one())
# # print(t1.get_first())
# t1 = Themes(['sun', 'feeling'])
# t1.add_theme('cool')
# t1.shift_one()
# print(t1.get_first())
# t1.reverse_order()
# print(t1.get_themes())

# Класс "Одномерный массив" TArray
#
#       Класс содержит поле для задания количества элементов и поле для хранения элементов массива.
#   Методы:
#   - конструктор без параметров, конструктор с параметрами, конструктор копирования
#   - ввод и вывод данных
#   - поиск максимального и минимального значений
#   - сортировка массива
#   - поиск суммы элементов
#   - перегрузка оператора + (добавление элемента)
#   - перегрузка оператора * (умножение элементов массива на число)
#
# class TArray:
#
#     def __init__(self, num, elem : list):
#         self.num = num
#         self.elem = elem
#
#     def copy_constructor(self,elem):
#         return copy.copy(elem)
#
#     def input_method(self, num):
#         for i in range(0,num):
#             a = int(input("Ввод данных: "))
#             self.elem.append(a)
#         return self.elem
#
#     def get_method(self):
#         return self.elem
#
#     def max_search(self):
#         max = self.elem[0]
#         min = self.elem[0]
#         for i in self.elem:
#             if i > max:
#                 max = i
#             if i < min:
#                 min = i
#         return max, min
#
#     def sort_method(self):
#         self.elem.sort()
#         return self.elem
#
#     def sum_method(self):
#         sum = 0
#         for i in self.elem:
#             sum += i
#         return sum
#
#     def __add__(self, other):
#         self.elem.append(other)
#         return self.elem
#
#     def __mul__(self, other):
#         new_elem = []
#         for i in self.elem:
#             new_elem.append(i * other)
#         return new_elem
#
# t = TArray(5,[])
# t.input_method(5)
# # print(t.get_method())
# # print(t.max_search())
# # print(t.sort_method())
# # print(t.sum_method())
# # print(t.__add__(2))
# # print(t.__mul__(2))
#
#
# Класс "Разговор"(Talking)
#
#   Экземпляр класса инициализируется с аргументом name - именем котенка. Класс реализует методы:
#   - to_answer() - ответить: котенок через один раз отвечает да или нет, начиная с да. Метод возвращает "moore-moore"
#   если да и "meow-meow", если нет. Одновременно увеличивает количество соответствующих ответов.
#   - number_yes() - количество ответов да.
#   - number_no() - количество ответов нет.
#
# class Talking:
#
#     def __init__(self, name):
#         self.name = name
#         self.number_yes = 0
#         self.number_no = 0
#         self.result = 0
#
#
#     def to_answer(self):
#         if self.result == 0:
#             self.result = 1
#             self.number_yes += 1
#             return "moore-moore"
#         else:
#             self.result = 0
#             self.number_no += 1
#             return "meow-meow"
#
#     def number_yes(self):
#         return self.number_yes
#
#     def number_no(self):
#         return self.number_no
#
# tk = Talking('Tomas')
# tk1 = Talking('Bob')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f"{tk.name} says 'yes' {tk.number_yes} times, 'no' {tk.number_no} times")
# print(tk.to_answer())
# print(tk1.to_answer())
# print(tk1.to_answer())
# # print(tk1.to_answer())
# print(f"{tk.name} says 'yes' {tk.number_yes} times, 'no' {tk.number_no} times")
# print(f"{tk1.name} says 'yes' {tk1.number_yes} times, 'no' {tk1.number_no} times")






