#Задача_2
my_value = str("100100")
my_symbol = '0'
my_value = my_value[::-1]
my_len = len(my_value)
for zero in range (my_len):
    if my_value[zero] == '0' :
       print (my_symbol)
    else: break
##############################################
#Задача_7
my_str = str('abcdn')
len_1 = len(my_str)
if len_1%2 == 1: my_str += '_'
len_1= len(my_str)
my_list = list(my_str)
my_result = []
for a in range (0, len_1-1, 2):
    my_result.append(my_list[a]+ my_list[a+1])
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

##############################################
