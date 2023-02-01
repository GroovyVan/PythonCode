# Quick functions
import sys
import timeit

measures = [
    (43,431),
    (132,123),
    (52,567),
    (678,44),
    (14689,3154)
]
# перемножение столбцов
# первый способ
def squares(measures):
    sqs = []
    for w_l in measures:
        print(w_l[0],w_l[1])
        sqs.append(w_l[0] * w_l[1])
    return sqs
print(squares(measures))

# второй способ
p = [w_l[0] * w_l[1] for w_l in measures]
print(p)

# третий способ
m = map(lambda w_l: w_l[0] * w_l[1], measures)
print(m)
print(list(m))

print('-' * 100)

#print('sqs_size', sys.getsizeof(sqs(measures)))
#sqs_time = timeit.timeit(sqs(measures), number = 10)
#print('sqs_time', sqs_time)

print('list_size', sys.getsizeof(p))
p_list =
p = [w_l[0] * w_l[1] for w_l in measures]
p_time = timeit.timeit(p_list, number = 1)
print('p_time', p_time)

#print('map_size', sys.getsizeof(list(m)))
#m_map = map(lambda w_l: w_l[0] * w_l[1], measures)
#m_time = timeit.timeit(m_map, number = 10)
#print('m_time', m_time)