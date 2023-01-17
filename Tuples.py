# Tuples

#виды
#a = tuple()
#b = ()
#print(a)
#print(b)

a = ()
b = (1,)
c = (2, 3)
d = (4, 5, 6)
#print(a)
#print(b)
#print(c)
#print(d)

#x, y, z = d
#print(x)
#print(y)
#print(z)

#обмен значений переменных
l = 40
r = 12
l, r = r, l
#print(l)
#print(r)

#можно складывать и умножать
p = (b + c + d) * 5
print(p)

print(p[0])
print(p[5])
print(p[-1])
print(p[::-1])
print(p[1:20])
print(p[-4:-2])

#кол-во повторений элемента в кортеже
#print(p.count(6))

#индекс первого элемента значения функции
#print(p.index(2))

#удаление
#del a
#print(a)