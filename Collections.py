# Collections
import sys
import timeit
# все виды коллекций
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
c = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}
d = set(a)
# кол-во памяти, выделяемой для коллекций (подключаем модуль sys)
print('list_size', sys.getsizeof(a))
print('tuple_size', sys.getsizeof(b))
print('dict_size', sys.getsizeof(c))
print('set_size', sys.getsizeof(d))

print('---'* 10)
# скорость создания коллекций (подключаем модуль timeit)
a_list = '''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'''
a_time = timeit.timeit(a_list, number = 10000000)
print('a_time', a_time)

b_tuple = '''
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)'''
b_time = timeit.timeit(b_tuple, number = 10000000)
print('b_time', b_time)

c_dict = '''
c = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}'''
c_time = timeit.timeit(c_dict, number = 10000000)
print('c_time', c_time)

d_set = '''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'''
print(d_set)
d_time = timeit.timeit(d_set, number = 10000000)
print('d_time', d_time)

#?почему-то сет стал быстрее чем list и dict?