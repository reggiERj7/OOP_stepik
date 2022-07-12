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