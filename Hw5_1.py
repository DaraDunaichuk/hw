Задача_1
my_value = 100
my_str=str(my_value)
my_symbol = '0'
my_str = my_str.count(my_symbol)
print(my_str)
############################################

#Задача_2
my_value = "100100"
my_symbol = '0'
my_value = my_value[::-1]
for my_symbol in my_value:
    if my_symbol == '0':
        print (my_symbol)
    else: break
#############################################
Задача3

my_list_1 =[1, 2, 3, 4, 5, 6]
my_list_2 =[11, 2, 13, 14, 15, 16]
my_result = []
for symbol in my_list_1:
      if not symbol % 2:
        my_result.append(my_list_1[symbol])
# for symbol_1 in range [my_list_2]:
#       if symbol_1 % 2:
#          my_result.append(my_list_2[symbol_1])
print(symbol)

my_list_1 =[1, 2, 3, 4, 5, 6]
my_list_2 =[7, 8, 9, 10, 11, 12]
my_result = []
for value in my_list_1:
    if not value % 2:
        my_result.append(value)
for value_ in my_list_2:
    if value_ % 2:
        my_result.append(value_)
print(my_result)

##############################################
#Задача4
my_list =[1, 2, 3, 4, 5, 6]
my_new_list = my_list[1:-1]
my_new_list.append(my_list[0])
print(my_new_list)

##############################################
Задача5
my_list =[1, 2, 3, 4, 5, 6]
my_list[-1],my_list[0]=my_list[0],my_list[-1]
print(my_list)

##############################################
Задача6
my_str = (' 43 больше чем 34, но меньше чем 56 ')
my_list = my_str.replace(","," ").split( )
suma = 0
for digit in my_list:
    if digit.isdigit():
         suma += int(digit)
print(suma)
############################
# #Задача_7
my_str = 'abcdn'
i = int(0)
len = len(my_str)
my_result = []
if len%2:
    my_str += '_'
my_list = list(my_str)
for value in my_list[::2]:
    my_result.append(my_list[i]+ my_list[i+1])
    i += 2
print(my_result)

##############################################
#Задача_8

my_str = str('my long str')
l_limit = str('o')
r_limit= str('t')
sub_str = str()
i = len(my_str)
b=  int(-1)

for index in range(i):
    b += 1
    if l_limit == my_str[index]:
        for index in range(b,i):
            sub_str = sub_str + my_str[index]
            if r_limit == my_str[index]:
                break
sub_str = sub_str[1:-1]
print(sub_str)

#############################################

##############################################
#Задача_9
my_str = str('my long string')
my_str_1 = my_str[::-1]
l_limit = str('o')
r_limit= str('g')
sub_str = str()
my_len = len(my_str)
a= int(-1)
b= int(-1)
for index in range(my_len):
    a+=10
    if l_limit == my_str[index]:
        break
for index in range(my_len):
    b+=1
    if r_limit == my_str_1[index]:
        break
c = my_len - b
for index in range (a,c):
    sub_str = sub_str + my_str[index]
sub_str = sub_str[1:-1]
print(sub_str)

##############################################
#Задача_10

my_list = [2,4,1,5,3,9,0,7]
my_len = len(my_list)
sum = int(0)
for index in range(1, my_len - 2):
    if my_list[index] > my_list[index-1] and my_list[index] > my_list[index+1]:
        sum+=1
    else:
        continue
print(sum)
