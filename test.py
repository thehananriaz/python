# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def pass_fail(self):
#         if self.marks <= 40:
#             print("fail")
#         else:
#             print(" you pass")
#
#
# student1 = student("hanan", 21)
# print(student1.name, student1.marks)
#

#
# print(int.__add__(1,2))
# print(str.__add__("hello" , "world"))

#adding complex number

# class complexnumber:
#     def __init__(self,r,i):
#         self.real = r
#         self.imag = i
#     def __add__(self,x):
#         return f"{self.real+x.real} + {self.imag+x.imag}i"
#
# c1 = complexnumber(2,3)
# c2 = complexnumber(4,1)
# print(c1 + c2)

#iterables & iterators

# listt = [1,2,3,4,9,12,122]
# value = iter(listt)
#
# while(True):
#     try:
#         x = next(value)
#         print(x)
#     except:
#         print("no more elements")
#         break


# item = next(value)
# print(item)
# item1 = next(value)
# print(item1)

#
# for i in value:
#     print(i)

#generators

# def my_generator():
#     for i in range(100):
#         yield i
#
# g = my_generator()
# print(next(g))
# print(next(g))

#closure
# def outer_funtion():
#     def inner_funtion():
#         x=200
#         return x
#     return inner_funtion()
# print(outer_funtion())


#decorators in python

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("start before decoration")
#         fx(*args, **kwargs)
#         print("after decoration")
#     return mfx()
# def add(a,b):
#     print(a+b)
# @greet
# def afunction():
#     print("Hello World")
#
# greet(add(2,3))


#@property

# class employe:
#     def __init__(self,name,last):
#         self.name = name
#         self.last = last
#     @property
#     def email(self):
#
#         return (f"{self.name}{self.last}@gmail.com")
#     @property #getter to get the value from the method without changing the variables
#     def fullname(self):
#         return (f"{self.name} {self.last}")
#
#     @fullname.setter #setter
#     def fullname(self, naam):
#         name,last = naam.split()
#         self.name = name
#         self.last = last
#     @fullname.deleter #deleter
#     def fullname(self):
#         self.name = None
#         self.last = None
#
# e1 = employe("John","Doe")
# e1.fullname = "Hanan Riaz"
# print(e1.name)
#
# del e1.fullname
# print(e1.email)
# print(e1.fullname)


#RegEx
#
# import re
#
# pattern = r"[a-z]aba"
#
# text = '''The first day of aba jaba daba laba z is Eid al-Fitr, fasting is prohibited. Some Muslims observe six days of optional fasting during Shawwāl beginning the day after Eid ul-Fitr since fasting is prohibited on this day. These six days of fasting together with the Ramadan fasts, are equivalent to fasting all year round.
# '''
#
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match.span())
#     print(text[match.span()[0]:match.span()[1]])

import re
# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)
#
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")






