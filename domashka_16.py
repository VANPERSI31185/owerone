######################## EXEM_1 #####################

# Напишите функцию, которая
# будет принимать фамилию и
# показывать только первую
# букву.
# Буква должна быть заглавной.
# Остальные буквы должны
# заменяться звездочками.

# def surname(S):
#     c = ''
#     for i in range(0,len(S)):
#         if S[i].islower() and S[i-1].isalpha() == False or i == 0:
#             c += S[i].upper()
#         else:
#             c += "*"
#     return c
# S = input()
# print(surname(S))


####################### Hometask_14_8 ###########################


# Добавьте в класс Pet дескриптор,
# чтобы нельзя было задать
# отрицательный возраст или 0

# from abc import ABC, abstractmethod
#
#
# class Pet(ABC):
#
#     @abstractmethod
#     def age(self):
#         if int(input()) >= 1:
#             pass
#
#
# class Dog(Pet):
#     def age(self):
#         print("Woof! Woof!")
#
#
# class Cat(Pet):
#     def age(self):
#         print("Meow! Meow!")
#
#
# class Parrot(Pet):
#     def age(self):
#         print("Tweet! Tweet!")
#
#
# bobik = Dog()
# bobik.age()

####################### Hometask_14_8 ###########################

# Добавьте в класс Pet валидацию,
# чтобы у питомца было имя и хозяин.

from abc import ABC, abstractmethod


class Pet(ABC):

    @abstractmethod
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        pass


class Dog(Pet):
    def __set_name__(self, owner, name):
        print("Ivan","Bobik")


class Cat(Pet):
    def age(self):
        print("Meow! Meow!")


class Parrot(Pet):
    def age(self):
        print("Tweet! Tweet!")


bobik = Pet("Ivan","Bobik")
bobik1 = Dog("Ivan","Bobik")
bobik1.owner
bobik1.name