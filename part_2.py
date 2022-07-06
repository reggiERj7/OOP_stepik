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

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)
    
    def draw(self):
        print(*self.get_coords())

line = Line(1, 2, 3, 4)
line.draw()