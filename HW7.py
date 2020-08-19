#Задача#1
#########################
import random
my_list = []

value = int()
for value in range(20):
    some_int = random.randint(0, 100)
    my_list.append(some_int)
print(my_list)
#Задача#2
#############################
import random
x= random.randint(0,10)
x_1 = random.randint(0,10)
x_2 = random.randint(0,10)
y= random.randint(0,10)
y_1= random.randint(0,10)
y_2 = random.randint(0,10)
triangle = {'A': (x,y),'B':(x_1,y_1) ,'C':(x_2,y_2)}
print(triangle)

#Задача#3
#############################

def my_print ():
#     my_str = "I'm the string"
#     my_str_1 = ('***'+my_str+'***')
#     print(my_str_1)
# print(my_print())
#Задача#3
#############################
my_str = "I'm the string"
my_print = str()
my_print = ('***'+my_str+'***')
print(my_print)
#Задача#4
#############################

def my_print ():
    my_str = "I'm the string"
    i= len(my_str)
    my_str_1 = ('*'*i + '\n'+ my_str + '\n' + '*'*i)
    print(my_str_1)
print(my_print())

#Задача#4
#############################

my_str = "I'm the string"
my_print=str()
i= len(my_str)
my_print = ('*'*i + '\n'+ my_str + '\n' + '*'*i)
print(my_print)
#Задача#5
#############################

def my_print ():
    my_str = "I'm the string"
    i= len(my_str)
    my_str_1 = ('*'*i + '\n'+ '***'+ my_str + '***' + '\n' + '*'*i)
    print(my_str_1)
print(my_print())

#Задача#5
#############################
my_str = "I'm the string"
my_print=str()
i= len(my_str)
my_print = ('*'*i + '\n'+ '***'+ my_str + '***' + '\n' + '*'*i)
print(my_print)
