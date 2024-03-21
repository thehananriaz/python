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
def outer_funtion():
    def inner_funtion():
        x=200
        return x
    return inner_funtion()
print(outer_funtion())






