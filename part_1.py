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
sdsf
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