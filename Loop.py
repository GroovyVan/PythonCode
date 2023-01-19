# Loops

a = [
    {'name': 'Ann', 'age': '22'},
    {'name': 'Ben', 'age': '13'},
    {'name': 'Max', 'age': '13'},
    {'name': 'Ed', 'age': '11'},
    {'name': 'Alex', 'age': '23'},
    {'name': 'Max', 'age': '155'},
    {'name': 'Mona', 'age': '16'},
    {'name': 'Eric', 'age': '14'}
]

    #первый способ. простая но не подходящая для большого кол-ва данных
#if a[0]['name'] == 'Max':
#    a[0]['age'] = 10

#if a[1]['name'] == 'Max':
#    a[1]['age'] = 10

#if a[2]['name'] == 'Max':
#    a[2]['age'] = 10

#if a[3]['name'] == 'Max':
#    a[3]['age'] = 10

#if a[4]['name'] == 'Max':
#    a[4]['age'] = 10

#if a[5]['name'] == 'Max':
#    a[5]['age'] = 10

#if a[6]['name'] == 'Max':
#    a[6]['age'] = 10

    #второй способ
#index = 0
#while index < len(a):
#    if a[index]['name'] == 'Max':
#        a[index]['age'] = 10
#    index += 1 #если = 0 то будет выполняться бесконечно

    #третий способ
# r = range [start:stop(not inc):step(def = 1]
#for index in range(len(a)):
#    if a[index]['name'] == 'Max':
#        a[index]['age'] = 10

    #четвертый способ
for b in a:
    if b['name'] == 'Max':
        b['age'] = 10
    #при одинаковых значениях имен и тп
        break
else:
    print('Invalid name')

print(a)