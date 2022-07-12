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

# class Museum:

#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []

#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)

#     def remove_exhibit(self, obj):
#         if obj in self.exhibits:
#             self.exhibits.remove(obj)
    
#     def get_info_exhibit(self, indx):
#         if self.exhibits[indx]:
#             return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
    
# class Picture:

#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr

# class Mummies:

#     def __init__(self, name, location, descr):
#         self.name = name
#         self.author = location
#         self.descr = descr

# class Papyri:

#     def __init__(self, name, date, descr):
#         self.name = name
#         self.author = date
#         self.descr = descr

# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)


###########################  ПОДВИГ 7

# class SmartPhone:

#     def __init__(self, model) -> None:
#         self.model = model
#         self.apps = []

#     def add_app(self, app):
#         if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
#             if app not in self.apps:
#                 self.apps.append(app)
        
#     def remove_app(self, app):
#         if app in self.apps:
#             self.apps.remove(app)
    
# class AppVK:

#     def __init__(self, name = 'ВКонтакте') -> None:
#         self.name = name
    
# class AppYouTube:

#     def __init__(self, memory_max, name = 'YouTube') -> None:
#         self.name = name
#         self.memory_max = memory_max
        
# class AppPhone:

#     def __init__(self, phone_list = {}, name = 'Phone') -> None:
#         self.name = name
#         self.phone_list = phone_list
        
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# print(sm.__dict__)
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)

###########################  ПОДВИГ 8 (РЕШИЛ ПРАВИЛЬНО, НО СТЕПИК НЕ ПРИНИМАЕТ)

# class Circle:

#     attrs = {'x': (int, float), 'y': (int, float), 'radius': (int, float)}

#     def __init__(self, x, y, radius):
#         self.__x = self.__y = self.__radius = None
#         self.__x = x
#         self.__y = y
#         self.__radius = radius

#     @property
#     def x(self):
#         return self.__x
        
#     @x.setter
#     def x(self, value):
#         self.__x = value

#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, value):
#         self.__y = value

#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def radius(self, value):
#         self.__radius = value
    
#     def __setattr__(self, key, value):
#         if key in self.attrs and type(value) not in self.attrs[key]:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'radius' and value <= 0:
#             return
#         super().__setattr__(key, value)

#     def __getattr__(self, item):
#         return False


# circle = Circle(10.5, 7, 22)
# circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name # False, т.к. атрибут name не существует
# print(circle.__dict__)


###########################  ПОДВИГ 9

# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000

#     def __init__(self, a, b, c) -> None:
#         self.__a = self.__b = self.__c = None
#         self.__a = a
#         self.__b = b
#         self.__c = c

#     @classmethod
#     def verify_coords(cls, value):
#         return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION and type(value) in (int, float)

#     @property
#     def a(self):
#         return self.__a    

#     @a.setter
#     def a(self, value):
#         if self.verify_coords(value):
#             self.__a = value
    
#     @property
#     def b(self):
#         return self.__b    

#     @b.setter
#     def b(self, value):
#         if self.verify_coords(value):
#             self.__b = value
    
#     @property
#     def c(self):
#         return self.__c    

#     @c.setter
#     def c(self, value):
#         if self.verify_coords(value):
#             self.__c = value

#     def __setattr__(self, key, value):
#         if key in ('MAX_DIMENSION', 'MIN_DIMENSION'):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         super().__setattr__(key, value)

# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(a,b,c)
# d.MAX_DIMENSION = 10  # исключение AttributeError

        