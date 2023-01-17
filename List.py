# Lists

a = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
b = [2, 3, 4, 5, 6, 7, 8, 9]
#    0   1   2   3   4   5   6   7   8   9

#print(a[1])
#print(a[2])
#print(a[3])
#print(a[4])
#print(a[5])
#print(a[6])
#print(a[7])
#print(a[8])
#print(a[9])

#кол-во элементов
#print(len(a))

#элемет с конца
#print(len(a))
#print(a[len(a)-1])
#print(a[-1])

#срезы
#b = a[0:10]
#print(b)

#только четные элементы
#b = a[::2]
#print(b)

#элементы в обратном порядке
#b = a[::-1]
#print(b)

#добавляет в конец списка
#a.append('добавляет в конец списка')
#print(a)

#добавляет в указанную часть списка
#a.insert(1,'добавляет в указанную часть списка')
#print(a)

#убирает элемент
#a.remove(55)
#print(a)

#del a[0]
#print(a)

#a.pop(8)
#print(a)

#сложение списков
#print(a + b)
#print(b + a)

#a.extend(b)
#print(a)

#переназначение элемента
#a[4] = 999
#print(a)

c = [6]
e = c
c.append(2)
print(c)
print(e)