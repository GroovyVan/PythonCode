# Comparsion operators

a = 4
b = 9

a1 = a == b #равенстао
a2 = a != b #неравенство
a3 = a > b
a4 = a < b
#print(a1,a2,a3,a4)

#if true_expection:
    # do something
#else
    # do something else



#if a3:
   # print('a больше чем b')
#else:
   # print('a меньше чем b')

#if a < b:
#    print('a меньше чем b')
#else:
#    print('a больше чем b')

#if a < b:
#    print('a меньше чем b')
#elif a > b:
#    print('a больше чем b')
#else:
#    print('значения равны')

a = int(input('введите а: '))
b = int(input('введите b: '))
if a < b:
    print('a меньше чем b')
elif a > b:
    print('a больше чем b')
else:
    print('значения равны')