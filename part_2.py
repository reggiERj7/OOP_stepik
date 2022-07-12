########### 2.1  Режимы доступа public, private, protected. Сеттеры и геттеры

####### ПОДВИГ 3

# class Clock:

#     def __init__(self, time = 0):
#         self.__time = time

#     def __check_time(self, tm):
#         if type(self.__time) == int and 0 <= tm < 100000:
#             return True
#         return False

#     def get_time(self):
#         return self.__time

#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm

# clock = Clock(4530)
# print(clock.get_time())

####### ПОДВИГ 4


# class Money:

#     def __init__(self, money: int):
#         if self.__check_money(money):
#             self.__money = money


#     def __check_money(self, money: int) -> bool:
#         if isinstance(money, int) and money >= 0:
#             return True
#         return False

#     def set_money(self, money: int):
#         if self.__check_money(money):
#             self.__money = money
    
#     def get_money(self):
#         return self.__money
    
#     def add_money(self, mn: object):
#         self.__money += mn.get_money()


# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = print(mn_1.get_money())    # 100
# m2 = print(mn_2.get_money())    # 120   



####### ПОДВИГ 6


# class Book:

#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price

#     def set_title(self, title: str):
#         self.__title = title

#     def set_author(self, author: str):
#         self.__author = author

#     def set_price(self, price: int):
#         self.__price = price

#     def get_title(self) -> str:
#         return self.__title
    
#     def get_author(self) -> str:
#         return self.__author
    
#     def get_price(self) -> int:
#         return self.__price
    

####### ПОДВИГ 7

# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
    
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
    
#     def get_coords(self):
#         return (self.__x1, self.__y1, self.__x2, self.__y2)
    
#     def draw(self):
#         print(*self.get_coords())

# line = Line(1, 2, 3, 4)
# line.draw()


################# 2.2 Свойства property. Декоратор @property


###########################  ПОДВИГ 4


# class Car:

#     def __init__(self):
#         self.__model = None

#     @property
#     def model(self):
#         return self.__model
    
#     @model.setter
#     def model(self, model):
#         if isinstance(model, str) and 2 < len(model) < 100:
#             self.__model = model
        
# car = Car()
# car.model = 'Toyota'
# print(car.model)
    

###########################  ПОДВИГ 5

# class WindowDlg:

#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__height = self.__width = None
#         self.__width = width
#         self.__height = height


#     def show(self):
#         return f"{self.__title}: {self.width}, {self.height}"

#     @property
#     def width(self):
#         return self.__width
    
#     @width.setter
#     def width(self, width):
#         if isinstance(width, int) and 0 <= width <= 10000:
#             if self.__width:
#                 self.show()
#             self.__width = width


#     @property
#     def height(self):
#         return self.__height
    
#     @height.setter
#     def height(self, height):
#          if isinstance(height, int) and 0 <= height <= 10000:
#             if self.__height:
#                 self.show()
#             self.__height = height
    

###########################  ПОДВИГ 7

# class RadiusVector2D:

#     MIN_COORD = -100
#     MAX_COORD = 1024

#     def __init__(self, x = 0 , y = 0):
#         self.__x = self.__y = 0
#         self.__y = y
#         self.__x = x
    
#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, value):
#         if self.__is_verify(value):
#             self.__x = value
    
#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, value):
#         if self.__is_verify(value):
#             self.__y = value
    
#     @staticmethod
#     def norm2(vector):
#         return vector.x*vector.x + vector.y*vector.y
    
#     @classmethod
#     def __is_verify(cls, value):
#         return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

# v1 = RadiusVector2D(-102,2000)    
# print(RadiusVector2D.norm2(v1))


###########################  ПОДВИГ 10

# class PhoneBook:

#     def __init__(self):
#         self.__list = []


#     def add_phone(self, phone: dict):
#         self.__list.append(phone)
    
#     def remove_phone(self, indx: int):
#         if self.__list[indx]:
#             self.__list.pop(indx)

#     def get_phone(self):
#         return self.__list


# class PhoneNumber:

#     def __init__(self, number: int, fio: str):
#         self.number = number
#         self.fio = fio


# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# # p.remove_phone(0)
# print(p.get_phone())

###########################  ПОДВИГ 9

# class LineTo:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class PathLines:

#     def __init__(self, *args):
#         self.coords = list((LineTo(0, 0), ) + args)
    
#     def get_path(self):
#         return self.coords[1:]

#     def get_length(self):
#         tmp = ((self.coords[i-1], self.coords[i]) for i in range(1, len(self.coords)))
#         return sum(map(lambda k: ((k[0].x - k[1].x)**2 + (k[0].y - k[1].y)**2)**0.5, tmp))        

#     def add_line(self, line):
#         self.coords.append(line)


################# 3.1 Методы __setattr__, __getattribute__, __getattr__ и __delattr__

###########################  ПОДВИГ 3

# class Book:

#     attrs = {'title': str, 'author': str, 'pages': int, 'year': int}
    
#     def __init__(self, title = '', author = '', pages = 0, year = 0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year

#     def __setattr__(self, name, value):
#         if name in self.attrs and self.attrs[name] == type(value):
#             super().__setattr__(name, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")


# book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)


###########################  ПОДВИГ 4

# class Shop:

#     def __init__(self, title):
#         self.goods = []
#         self.title = title

#     def add_product(self, product):
#         self.goods.append(product)
    
#     def remove_product(self, product):
#         if product in self.goods:
#             self.goods.remove(produc)

# class Product:

#     attrs = {'name': (str,), 'weight': (int, float), 'price': (int, float)}
#     _id_instance = 1

#     def __init__(self, name, weight, price):
#         self.id = Product._id_instance
#         Product._id_instance += 1

#         self.name = name
#         self.weight = weight
#         self.price = price

#     def __setattr__(self, key, value):
#         if key in self.attrs and type(value) in self.attrs[key]:
#             if (key == 'weight' or key == 'price') and value <= 0:
#                 raise TypeError("Неверный тип присваиваемых данных.")
#         elif key in self.attrs:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         super().__setattr__(key, value)

#     def __delattr__(self, item):
#         if item == 'id':
#             raise AttributeError("Атрибут id удалять запрещено.")

# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")


###########################  ПОДВИГ 5

# class LessonItem:

#     attrs = {'title': str, 'practices': int, 'duration': int}

#     def __init__(self, title, practices, duration):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
    
#     def __setattr__(self, key, value):
#         if key in self.attrs and type(value) == self.attrs[key]:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
    
#     def __getattr__(self, item):
#         return False
    
#     def __delattr__(self, item):
#         if item in ('title', 'practices', 'duration'):
#             return False

# class Module:

#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
    
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
    
#     def remove_lesson(self, indx):
#         if self.lessons[indx]:
#             self.lessons.pop(indx)
    

# class Course:

#     def __init__(self, name):
#         self.name = name
#         self.modules = []

#     def add_module(self, module):
#         self.modules.append(module)
    
#     def remove_module(self, indx):
#         if self.modules[indx]:
#             self.modules.pop(indx)


# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)
# print(course.__dict__)
# print(module_1.__dict__)
# print(module_2.__dict__)

###########################  ПОДВИГ 6

class Museum:

    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)
    
    def get_info_exhibit(self, indx):
        if self.exhibits[indx]:
            return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
    
class Picture:

    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr
    
mus = Museum('Эрмитаж')
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
print(mus.get_info_exhibit(0))