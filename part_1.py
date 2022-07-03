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


