# ------------------------------1--------------------------------------

my_int = 5
my_float = 1.2
my_str = "Hello world"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Moscow', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')

# -------------------------2---------------------------------------------

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

# ------------------------3--------------------------------------
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("enter the number between 1 and 12: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("error")

# ---------------------4------------------------------------------

my_str = input("введите строку ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

# ----------------------5------------------------------------------

number = int(input("Enter number: "))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)


# ------------------------6--------------------------------------------

goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
