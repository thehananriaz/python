
'''
#variables

num1=10
num2=20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
print(num1//num2)
print(num1)

print(num1==num2)


f= False
t=True
d= None
print(d)


#strings

name= "hanan"
print(name[0:3])
print(name.capitalize())
print(name.upper())
print(name.isnumeric())


#input
num=input("enter number:")
print(num)

print("6+ number =",6+ int(num))



#list

l1= [1,7,8,9,45, "hanan"]

l1.extend([69,87])
print(l1)

print(type(l1))

#tupple

t=(3,6,7,8,90) #immutable

#sets
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10}
print(a.intersection(b))

#dictionaries
a = {"good": "something good", "bad": "something bad"}
b= {"hanan":21, "ahtisham":32}

print(a["good"])

print(b.get("ahtisham"))


#iftstatement

age = int(input("enter your age = "))

if (age>18):
    print("you are eligible")
elif (age<10):
    print("please no")
else:
    print("you are not")

print("end") 

#match case

a = int(input("enter integer = "))

match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case _:
        print("not found")

#forloop
s= [1,2,3,4,5,6,7,8,9]
a={21,2,9}
for i in a:
    print(i)

#whileloop

i=0
while (i<10):
    print(i)
    i+=1
while(True):
    i=int(input("enter integer = "))
    print(i)
    if(i==0):
        break
    for i in range(5):
    i+=1
    print(i)
i=2
while(i<10):
    i+=1
    print(i)
    
def greethello( name,ending):
    print("Hello" + name + ending)
    print("Hello")
    print("Hello")
    print(ending)

    print("function finish")

greethello( "John","hanna")

print("after function")

greethello( "hanannnn   ","live")


#functions

def letter(name, date):
    st= f"Hello my name is {name} \n and i will be absent on {date}"
    st2= ("hello my name is" + name + "\n i need leave for " + date)
    print(st)

name= input("enter your name: ")
date= input("enter date: ")

letter(name,date)

#try exceptional handling

try:
    name= int(input("enter your age: "))
    print("your agr is: " , name)
except Exception as e:
    print("invalid", e)
    
    
   with open("hanan.txt", "w") as f:
    f.write("hanan is my name")

with open("hanan.txt", "r") as f:
    s= f.read()
    print(s) 


#file io

with open("hanan.txt", "w") as f:
    f.write("Jinna na twadi mahnat wekhi ae \n ohi twadi kamyabi di qeemat janday nay \n  bakiyan lai tay tusi ek khush kismat ho")

with open("hanan.txt", "r") as f:
    s= f.read()
    print(s)
    
    
#opp

class person:
  def __init__(self,n,a):
     print("test")
     self.name= n
     self.age=a
  def info(self):
     print(self.name, "is " , self.age ,"year old")

a = person("hanan", "21")
b=person ("haris", "32")
a.info()
b.info()    
    

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

double = lambda x: x*2
print(double(5))

avg= lambda x,c,v: (x+c+v)/2
print(avg(3,3,3))

import pandas
import hashlib


def funp():
    print ("test")

funp()

def printfun():
    print("test")

printfun()

#dir 
x = (1,2,3)

print(dir(x))


class person():
    def __init__(self, name,age):
        self.name=name
        self.age=age

p1= person("hanan",21)
print(p1.__dict__)

print(help(person))
#inheritance
class employee:
    def __init__ (self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"the name is {self.name} for id is {self.id})")
class singer(employee):
    def __init__(self,genre):
        self.genre=genre

class artist(employee, singer):
    def __init__(self):
        print(f"{self.name} is a singer who'sgenre is {self.genre}" )


e= artist("hanan",21)
e.show()git c


#timemodule


def usingwhile():
    i = 0
    while i<50000:
       i = i+1
       print(i)
def usingfor():
   for i in range(50000):
     print(i)

init = time.time()
usingfor()
t= print(time.time()-init)
init = time.time()
usingwhile()
print(time.time()-init)
print(t)


#sleep time
print("hanan")
time.sleep(3)
print("hanan after 3 sec")

#time.strf

t = time.localtime()
ft = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(ft)

t = time.localtime()
ft = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(ft)

from datetime import datetime
corr=datetime.now()
print(corr)F

#strp time
current = '2019/05/30 4:32:51'
print(datetime.strptime(current , '%Y-%m-%d %H:%M:%S'))

from datetime import datetime

ts =13098341
t= datetime.fromtimestamp(ts)
print(t)


import datetime
import time
ct =datetime.datetime.now()
ct =ct.strftime("%Y/%m-%d %H:%M:%S")
print(ct)


'''






































