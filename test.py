import random

id1 = '123'
id2 = '456'
names = ['rr', 'tt', 'zz']

with open('base.txt', 'a') as f:
    f.write(id1+':'+random.choice(names)+'\n')

with open('base.txt', 'a') as f:
    f.write(id2+':'+random.choice(names)+'\n')

# d = {}
# with open("base.txt") as file:
#     for line in file:
#         key, *value = line.strip().split(':')
#         if key in d:
#             d[key].append(value[0])
#         else:
#             d[key] = value
    
# print(d)
class nam:
    name = ''

def check():
    with open("base.txt") as file:
        for line in file:
            if '123' in line.strip().split(':'):
                nam.name = line.strip().split(':')[1]
                return nam.name
            else:
                return False

def double_check():
    if check() == False:
        print('no')
    else:
        print(nam.name)

double_check()