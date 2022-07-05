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

##################### 1.8 ИСПЫТАНИЕ СВОЙСТВАМИ И МЕТОДАМИ
# class Router:

#     def __init__(self):
#         self.buffer = []
#         self.servers = {}

#     def link(self, server):
#         self.servers[server.ip] = server
#         server.router = self
    
#     def unlink(self, server):
#         tmp = self.servers.pop(server.ip, False)
#         if tmp:
#             tmp.router = None

#     def send_data(self):
#         for i in self.buffer:
#             if i.ip in self.servers:
#                 self.servers[i.ip].buffer.append(i)
#         self.buffer.clear()
    
# class Server:

#     n = 1
#     def __init__(self):
#         self.buffer = []
#         self.ip = Server.n
#         Server.n += 1
#         self.router = None

#     def send_data(self, data):
#         if self.router:
#             self.router.buffer.append(data)

#     def get_data(self):
#         b = self.buffer[:]
#         self.buffer.clear()
#         return b
        
#     def get_ip(self):
#         return self.ip

# class Data:
#     def __init__(self, data, ip):
#         self.data = data
#         self.ip = ip

# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# # router.link(Server())
# # router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()