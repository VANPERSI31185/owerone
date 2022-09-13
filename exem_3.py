#################### exam_3_1 ########################

# Напишите функцию, которая
# будет принимать номер
# кредитной карты и показывать
# только последние 4 цифры.
# Остальные цифры должны
# заменяться звездочками

# def card_hide(card):
#     return '*' * len(card[:-4]) + card[-4:]
# print(card_hide("5456789515658562"))


################### exam_3_2 ########################

# Напишите функцию, которая
# проверяет: является ли слово
# палиндромом

# def is_palindrome(data):
#     data = data.replace('summer','шалаш').lower()
#     return True if data == data[::-1] else False
# print(is_palindrome("summer"))
# print(is_palindrome("шалаш"))


#################### exam_3_3 ########################

# Напишите классы Круг,
# Прямоугольник, Квадрат.
# Каждый класс должен
# содержать метод нахождения
# площади фигуры.
# Используйте
# :
# - Наследование - Абстрактный класс
# и методы
# - Округлите площадь круга до 2х чисел после запятой - Число π возьмите из модуля
# math

# from abc import ABC, abstractmethod
# import math
#
# class Figures(ABC):
#
#     @abstractmethod
#     def square(self):
#         pass
#
# class A_circle(Figures):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def square(self):
#         return round(math.pi * self.radius**2, 2)
#
# class Rectangle(Figures):
#
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#
#     def square(self):
#         return self.lenght * self.width
#
# class A_square(Figures):
#
#     def __init__(self, lenn):
#         self.lenn = lenn
#
#     def square(self):
#         return self.lenn**2
#
# a = A_circle(3)
# b = Rectangle(2,6)
# c = A_square(4)
# print(f"Площадь квадрата = ",c.square())
# print(f"Площадь прямоугольника = ",b.square())
# print(f"Площадь круга равна = ",a.square())



# Площадь квадрата = 16
# Площаль прямоугольника = 12
# Площадь круга равна = 28.27