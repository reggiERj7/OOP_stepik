# 1.3 Классы и объекты. Атрибуты классов и объектов.

######################## Подвиг 8

# class TravelBlog:
#     total_blogs = 0

# tb1 = TravelBlog()
# tb1.name, tb1.days = 'Франция', 6
# # print(getattr(tb1, 'days'))
# setattr(TravelBlog, 'total_blogs', 1)
# tb2 = TravelBlog()
# tb2.name, tb2.days = 'Италия', 5
# setattr(TravelBlog, 'total_blogs', 2)
# print(getattr(TravelBlog, 'total_blogs'))

######################## Подвиг 9
# class Figure:
#     type_fig = 'ellipse'
#     color = "red"

# fig1 = Figure()

# fig1.start_pt, fig1.end_pt, fig1.color = (10,5), (100,20), 'blue'
# delattr(fig1, 'color')
# print(*fig1.__dict__)


######################## Подвиг 10

# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'

# p1 = Person()
# try:
#     p1.__dict__['job']
#     print(True)
# except:
#     print(False)


####### 1.4 МЕТОДЫ КЛАССОВ. ПАРАМЕТР SELF

######################## ПОДВИГ 4

# class MediaPlayer:
    
#     def open(self, file: str):
#         self.filename = file

#     def play(self) -> str:
#         return f"Воспроизведение {self.filename}"

# media1, media2 = MediaPlayer(), MediaPlayer()

# media1.open('filemedia1')
# media2.open('filemedia2')

# print(f"{media1.play()}\n{media2.play()}")


######################## ПОДВИГ 5

# from typing import List


# class Graph:
#     LIMIT_Y = [0, 10]

#     def set_data(self, data: List):
#         self.data = data

#     def draw(self) -> str:
#         a, b = self.LIMIT_Y
#         print(*filter(lambda x: a <= x <= b, self.data))

# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

######################## ПОДВИГ 7

# from typing import List


# class StreamData:
    
#     def create(self, fields: List, lst_values: List) -> bool:
#         if len(fields) != len(lst_values):
#             return False
#         for i, key in enumerate(fields):
#             setattr(self, key, lst_values[i])
#         return True


######################## ПОДВИГ 9

# import sys
# from typing import List

# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')

#     # здесь добавлять методы
#     def insert(self, data: List):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
    
#     def select(self, a: int, b: int):
#         return self.lst_data[a:b+1]


######################## ПОДВИГ 10

# class Translator:

#     def add(self, eng: str, rus: str):
#         if 'dic' not in self.__dict__:
#             self.dic = {}
#         self.dic.setdefault(eng, [])
#         self.dic[eng].append(rus)
    
#     def remove(self, eng: str):
#         self.dic.pop(eng, False)
    
#     def translate(self, eng: str):
#         return self.dic[eng]

# tr = Translator()

# tr.add('tree', 'дерево')
# tr.add('car', 'машина')
# tr.add('car', 'автомобиль')
# tr.add('leaf', 'лист')
# tr.add('river', 'река')
# tr.add('go', 'идти')
# tr.add('go', 'ехать')
# tr.add('go', 'ходить')
# tr.add('milk', 'молок')

# print(*tr.translate('go'))

####### 1.5 ИНИЦИАЛИЗАТОР __init__ и финализатор __del__

######################## ПОДВИГ 2

# class Money:

#     def __init__(self, money):
#         self.money = money


# my_money = Money(100)
# your_money = Money(1000)

######################## ПОДВИГ 3

# class Point:
#     def __init__(self, x: int, y: int, color = "black"):
#         self.x = x
#         self.y = y
#         self.color = color

#     def __del__(self):
#         pass
  
# points = [Point(2*i+1, 2*i+1) for i in range(0,1000)]
# points[1].color = 'yellow'


######################## ПОДВИГ 4

# import random
# class Line:
    
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)

# class Rect:
    
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)

# class Ellipse:
    
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)

# elements = [(Line, React, Ellipse)[random.randint(0, 2)](1,2,3,4) for i in range(217)]
# for k in elements:
#     if isinstance(k, Line):
#         k.sp = k.ep = 0,0


######################## ПОДВИГ 5

# class TriangleChecker:

#     dic = {}

#     def __init__(self, a: int, b: int, c: int):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.dic[f'{type(self.a)}'] = self.a
#         self.dic[f'{type(self.b)}'] = self.b
#         self.dic[f'{type(self.c)}'] = self.c

#     def is_triangle(self) -> int:
#         for key, value in self.dic.items():
#             if 'int' in key or 'float' in key or value <= 0:
#                 return 3
#         return 1

# a, b, c = map(float, input().split())
# print(a)
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


######################## ПОДВИГ 6


# class Graph:

#     def __init__(self, data):
#         self.data = data[:]
#         self.is_show = True

#     def set_data(self, data):
#         self.data = data[:]
    
#     def show_table(self):
#         print(" ".join(map(str, self.data)))

#     def show_graph(self):
#         print(f'Графическое отображение данных: {" ".join(map(str, self.data))}')

#     def show_bar(self):
#         print(f'Столбчатая диаграмма: {" ".join(map(str, self.data))}')

#     def set_show(self, fl_show = True):
#         self.is_show = fl_show
#         if self.is_show is False:
#             return 'Отображение данных закрыто'
     
# data_graph = list(map(int, input().split()))

# gr = Graph(data_graph)
# gr.show_bar()
# print(gr.set_show(False))


######################## ПОДВИГ 7

# class CPU:

#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr

# class Memory:

#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume

# class MotherBoard:

#     def __init__(self, name, cpu, *mems):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mems[:self.total_mem_slots]


#     def get_config(self):  
#         return [f'Материнская плата: {self.name}', 
#         f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}', 
#         f'Слотов памяти: {self.total_mem_slots}', 
#         'Память: ' + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))]


# mb = MotherBoard("MSI", CPU("Inteal", 4000), Memory('Patriot', 2500), Memory("patriot", 4000))
# mb.get_config()


######################## ПОДВИГ 8

# class Cart:
    
#     def __init__(self):
#         self.goods = []
    
#     def add(self, cart):
#         self.goods.append(cart)
    
#     def remove(self, indx):
#         self.goods.pop(indx)

#     def get_list(self):
#         return [f'{i.name}: {i.price}' for i in self.goods]

# class Table:
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class TV:
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Notebook:
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Cup:
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# cart = Cart()
# cart.add(Notebook("Lenovo", 4000)) 
# cart.add(Notebook("Lenovo", 4000)) 
# cart.add(TV("Samsung", 5000))
# cart.add(TV("LG", 55000))
# cart.add(Cup("Личная", 200))
# cart.add(Table("Личная", 200))