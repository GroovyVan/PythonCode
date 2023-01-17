# Sets

#a = set(['True', 5.4, 12, (54, 11), False ])
#a.add(13)
#a.add(54)
#print(a)
#print(len(a))

#сложение сетов
#b = set(['Hi', 'Hey', 'Hello', 1, 4 , 5.4])
#print(a.union(b))
#print(b.union(a))

id = [3, 6, 7, 1, 236, 7, 23, 5, 71, 4, 12, 6, 347, 28, 92, 64, 26, 21, 3, 1516916, 91, 601, 71, 718701 , 7, 18235, 846, 3268, 26]
data = [4, 1541, 6, 2727, 2646, 3, 7, 89, 5, 5, 23, 6, 8, 3, 13, 589, 9, 3, 0, 37]
a = set(id)
b = set(data)

#совпадающие
same = b.intersection(a)

#есть в одном но нет в другом
indiv = b.symmetric_difference(a)

print(same, 'a')
print(indiv, 'b')

