my_list = ['abc','dfg','ehu','dasha']
new_list = []
a = int()
for index, value in enumerate(my_list):
    a = int(index)
    if index%2:
      new_list.append((my_list[a])[::-1])
    else:  new_list.append(my_list[a])
print(new_list)

##############################################
#Задача2

my_list = ['abc','dfg','ehu','dasha', 'ardf']
new_list = []
for index, value in enumerate(my_list):
    if value[0] == 'a':
                new_list.append(value)
print(new_list)

##############################################
#Задача3

my_list = ['abc','dfg','ehu','dasha', 'ardf']
new_list = []
for index, value in enumerate(my_list):
    for symbol in value:
        if symbol == 'a':
            new_list.append(value)
            break
print(new_list)

##############################################
#Задача4

my_list = ['abc', 1, 8,'dfg','ehu','dasha', 15, 'ardf']
new_list = []
for index, value in enumerate(my_list):
    if type(value) == str:
                new_list.append(value)
print(new_list)

##############################################
#Задача5

my_str = 'aabbDDDc123Ad'
my_str=my_str.lower()
my_set = set(my_str)
for value in my_set:
    b= my_str.count(value)
    if b == 1:
        print(value)

##############################################

#Задача5

# my_str = 'aabbcDDD123A  d'
# my_str = my_str.lower()
# unique = []
# for symbol in my_str[::]:
#     if symbol not in unique:
#         unique.append(symbol)
#
# print(unique)
##############################################
#Задача6

str_1 = 'fghjkopuytf8'
str_2 = 'nsfdctrkhjmncc8'
set_1 = set(str_1)
set_2 = set(str_2)
print(set_1.intersection(set_2))

#Задача6

# my_str_1 = 'aabbcDDD123A  d'
# my_str_2 = 'hydhlyhglnxuiab'
# my_str_1 = my_str_1.lower()
# my_str_2 = my_str_2.lower()
# unique = []
# my_str = str()
# for symbol in my_str_1[::]:
#     if symbol  in my_str_2:
#         unique.append(symbol)
# for symbol in unique[::]:
#     if symbol not in my_str:
#         my_str=my_str+symbol
# print(my_str)

##############################################
#Задача7
str_1 = 'fferrt'
str_2 = 'eetw'
set_1 = set()
set_2 = set()
# my_str=my_str.lower()
for value_1 in str_1:
    b = str_1.count(value_1)
    if b == 1:
        set_1.add(value_1)
for value_2 in str_2:
    b = str_2.count(value_2)
    if b == 1:
          set_2.add(value_2)
print(set_1.intersection(set_2))

##############################################
#Задача8

person = {"Фамилия" : "Дунайчук",
          "Имя": "Дарья",
          "Возраст" : 31,
           "Проживание" : {"Страна": "Украина",
                           "Город" : "Днепр",
                           "Улица": "Калиновая"},
            "Работа" : {"Наличие": "Да",
            "Должность": "Экономист"}}

print(person["Возраст"])

##############################################
#Задача8
cake = {"Коржи" : {"Мука": "400 гр.",
                   "Молоко" : "200 мл.",
                       "Масло": " 70 гр.",
                       "Яйцо": "2 шт."},
        "Крем" : {"Сахар": "200 грн.",
                "Масло": "50 гр.",
                "Ваниль": "5 гр.",
                "Сметана": "200 мл."},
         "Глазурь": {"Какао": "50 гр.",
                     "Сахар": "100 гр.",
                     "Масло": "50 гр."}}
print(cake["Коржи"])